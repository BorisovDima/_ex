from twisted_.web import resource, server, static, xmlrpc
from twisted_.application import service, strports
from twisted_.internet import protocol, reactor, defer
from twisted_.protocols import basic
from zope.interface import implementer, Interface
from twisted_.python import components
from twisted_.spread import pb
from twisted_.internet import endpoints

import pwd


class ISetterService(Interface):

    def set_user(user, status):
        """
        Set User and his set status
        """


class IGetterService(Interface):

    def set_user(user, status):
        """
        Set User and his set status
        """


class GetterProto(basic.LineReceiver):
    def lineReceived(self, line):
        d = self.factory.get_user(line)
        d.addCallback(lambda r: self.sendLine(r))



class IGetterFactory(Interface):

    def get_user(user):
        """
        Return user
        """

    def get_users():
        """
        Return all the users
        """


@implementer(IGetterFactory)
class AdapterGetterFactory(protocol.ServerFactory):
    protocol = GetterProto

    def __init__(self, service):

        self.service = service
        self.users = service.users
        self.get_user = service.get_user
        self.get_users = service.get_users


components.registerAdapter(AdapterGetterFactory, IGetterService, IGetterFactory)



################################################

class SetterProto(basic.LineReceiver):
    def lineReceived(self, line):

        user, status = line.split(b',')
        self.factory.set_user(user, status)
        self.transport.loseConnection()



class ISetterFactory(Interface):

    def set_user(user, status):
        """
        Set User and his set status
        """


@implementer(ISetterFactory)
class AdapterSetterFactory(protocol.ServerFactory):
    protocol = SetterProto


    def __init__(self, service):
        self.service = service
        self.users = service.users
        self.set_user = self.service.set_user

components.registerAdapter(AdapterSetterFactory, ISetterService, ISetterFactory)


#############################################################################

class HttpTree(resource.Resource):
    def __init__(self, user):
        self.user = user
        super().__init__()

    def render_GET(self, request):
        return b'User %s' % self.user


class AdapterHttpTree(resource.Resource):
    def __init__(self, service):
        self.service = service
        self.users = service.users
        super().__init__()

    def getChild(self, path, request):
        user = self.service.get_user(path).result
        return HttpTree(user=user)


components.registerAdapter(AdapterHttpTree, IGetterService, resource.IResource)

#######################################################

class IXMLResource(Interface):
    pass

@implementer(IXMLResource)
class XMLR(xmlrpc.XMLRPC):
    def __init__(self, service):
        print(service)
        self.service = service
        super().__init__()

    def xmlrpc_getUser(self, user):
        return self.service.get_user(user)

    def xmlrpc_test(self, user):
        return []

components.registerAdapter(XMLR, IGetterService, IXMLResource)


###########################################################################


class IPerspective(Interface):


    def remote_get_user(user):
        """
        Return user
        """

    def remote_get_users():
        """
        Return all the users
        """

@implementer(IPerspective)
class PerspectiveB(pb.Root):
    def __init__(self, service):
        self.service = service
        super().__init__()


    def remote_get_user(self, user):
        return self.service.get_user(user)

    def remote_get_users(self):
        pass


components.registerAdapter(PerspectiveB, IGetterService, IPerspective)

#############################################################################

class Client(protocol.Protocol):

    def connectionMade(self):
        self.transport.write(b'root\r\n')
        print('TUTA')

    def dataReceived(self, data):
        print(data)



class ClientFactory(protocol.ClientFactory):
   protocol = Client

def client_made():
    f = ClientFactory()
    e = endpoints.TCP4ClientEndpoint(reactor, 'localhost', 8101)
    e.connect(f)




############################################################################
@implementer(IGetterService, ISetterService)
class FingerService(service.Service):
    def __init__(self):
        self.users = {}

    def get_user(self, user):
        return defer.maybeDeferred(lambda: self.users.get(user, b'Nothing'))

    def get_users(self):
        return defer.maybeDeferred(lambda: b', '.join(self.users.keys()))

    def set_user(self, user, status):
        self.users[user] = status


class AnotherBackend(FingerService):

    def get_user(self, user):
        try:
            user = pwd.getpwnam(user.decode()).pw_dir.encode()
        except Exception as e:
            print(e)
            user = b'Nothing'
        return defer.succeed(user)

f = AnotherBackend()




http_factory = server.Site(resource.IResource(f))
XML_factory = server.Site(IXMLResource(f))
pb_factory = pb.PBServerFactory(IPerspective(f))

reactor.listenTCP(8100, http_factory)
reactor.listenTCP(8101, IGetterFactory(f))
reactor.listenTCP(8102, ISetterFactory(f))
reactor.listenTCP(8103, XML_factory)
reactor.listenTCP(8104, pb_factory)


# e = endpoints.serverFromString(reactor, "ssl:port=443:certKey=cert.pem:privateKey=key.pem")
# e.listen(http_factory)
client_made()
reactor.run()

