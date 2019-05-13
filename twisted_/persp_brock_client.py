from twisted.spread import pb
from twisted.internet import reactor, defer

# client = pb.PBClientFactory()
# reactor.connectTCP('localhost', 8000, client)
# d = client.getRootObject()
#
#
#
# d.addCallback(lambda r: r.callRemote("one"))
# d.addCallback(lambda d: d.callRemote('two', 'Echo'))
# d.addCallback(lambda r: print(r))
# reactor.run()

######################################################


# class ref(pb.Referenceable):
#
#     def remote_turn(self, data):
#         print(data)
#
# client = pb.PBClientFactory()
# reactor.connectTCP('localhost', 8000, client)
# d = client.getRootObject()
# d.addCallback(lambda r: r.callRemote('rev', ref()) and r)
# d.addCallback(lambda r: r.callRemote('error'))
# d.addErrback(lambda err: print(err.getErrorMessage()))
# reactor.run()



client = pb.PBClientFactory()
reactor.connectTCP('localhost', 8104, client) # big_mixin_example.py
d = client.getRootObject()
d.addCallback(lambda r: r.callRemote('get_user', b'borisov'))
d.addCallback(lambda r: print(r))
reactor.run()

client = pb.PBClientFactory()
d = client.getRootObject()
d.addCallback(lambda r: r.callRemote(''))