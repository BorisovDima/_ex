from twisted.internet.defer import Deferred, inlineCallbacks, succeed
from twisted.internet import task
from twisted.internet import reactor
from copy import deepcopy

d1 = task.deferLater(reactor, 5, lambda : "END")


@inlineCallbacks
def defer(arg):
    print(arg)
    print('WAIT')
    r = yield d1
    print('FINISH')
    print(r)
    return r


def test():
    d = defer('Hello there')
    print(d)


# print(d, d1,  'DEFE')
# d.addCallback(lambda p: print(p))
# d.addCallback(lambda _:succeed('))))'))
# d.addCallback(lambda _:print(_))
test()
reactor.run()




