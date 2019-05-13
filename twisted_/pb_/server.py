from twisted.spread import pb
from twisted.internet import reactor



class Server(pb.Root):
    def remote_call(self, ref):
        print(ref)
        d = ref.callRemote('test')
        print(d)
        d.addCallback(lambda r: print(r))

    def remote_callDT(self):
        return {'coll': 'ection'}


factory = pb.PBServerFactory(Server())
reactor.listenTCP(8000, factory)
reactor.run()