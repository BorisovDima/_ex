from twisted.internet import defer, task, reactor

def sleep():
    return task.deferLater(reactor, 10, lambda : None)


@defer.inlineCallbacks
def racket(i):
    for i_ in range(3):
        yield sleep()
        print(i, i_)

@defer.inlineCallbacks
def test():
    yield defer.DeferredList([racket(i) for i in range(10)])



reactor.callLater(0, test)
reactor.run()
