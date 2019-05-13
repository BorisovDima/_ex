from twisted.spread import pb
from twisted.internet import reactor, defer



class MethodsF(pb.Root):

    def remote_test(self):
        print('WORK')
        return 'Result'


client = pb.PBClientFactory()
d = client.getRootObject()

@defer.inlineCallbacks
def callback(ref):
    d1 = yield ref.callRemote('call', MethodsF())
    d2 = yield ref.callRemote('callDT')
    print(d1, d2)



d.addCallback(callback)


reactor.connectTCP('localhost', 8000, client) # big_mixin_example.py
reactor.run()

