from twisted.internet import defer, reactor

#######################################################

def MyCallback(arg):
    return arg + ' 1'

def MyCallback2(arg):
    return arg + ' 2'


def MyCallback3(arg):
    print(arg, 3)


def MyErrback(err):
    print(err)

d = defer.Deferred()

d.addCallback(MyCallback) # 1 0
d.addCallback(MyCallback2)# 1 0
d.addCallback(MyCallback3)# 1 0 -  \/ error here?
d.addErrback(MyCallback3) # 0 1 - i can catch it  ( level + 1 )

d.callback('result')   # result = arg

######################################################

class TestAsync:

    def eventCall(self, data):
        self.d.errback(RuntimeError('error')) if data != 'ok' else self.d.callback('OK')

    def ok(self, data):
        print(f'OK {data}')
        reactor.stop()

    def error(self, data):
        print(f'error {data}')
        reactor.stop()

    def main(self):
        self.d = defer.Deferred()
        self.d.addCallbacks(self.ok, self.error)
        reactor.callLater(2, self.eventCall, 'oke')


# TestAsync().main()
# reactor.run()

########################   in loop  ###############################
from twisted.internet import task

call = reactor.callLater(3.5, lambda a: 0 , "hello, world")
call.cancel()

d = task.deferLater(reactor, 3.5, lambda a: 0, "hello, world")

loop = task.LoopingCall(lambda: print('loop'))
loopDeferred = loop.start(1.0)


d = task.deferLater(reactor, 3, lambda : print('OK'))
d.addTimeout(2, reactor)
d.addErrback(lambda e: print(e))


# reactor.run()
#############################################################################

d = defer.maybeDeferred(lambda : defer.succeed('12')) # is this deffer done?  return result or wait
d = defer.succeed('result')

###########################  in loop  ###################################################

from twisted.internet import threads

d = threads.deferToThread(lambda : [i for i in range(10000)]) # like executor
d.addCallback(lambda r: print(r))

# reactor.run()
###########################################

from twisted.internet.defer import ensureDeferred

async def coro():
    return []

d = ensureDeferred(coro())

d.addCallback(lambda r: print(r))

##############################################


d = defer.succeed('r')
d.addCallback(lambda r: print(r))
d.addCallback(lambda r: print(r))
print(d)


d = defer.Deferred()
d.addCallback(lambda r: r + 1)
d.addCallback(lambda r: r +1)
d.callback(0)
print(d)

################################################

d1 = defer.Deferred()
d2 = defer.Deferred()
d3 = defer.Deferred()


dl = defer.DeferredList([d1, d2, d3], consumeErrors=True)
     #defer.gatherResults([d1, d2, d3], consumeErrors=True)  # only success
d1.callback('OK')
d2.errback(RuntimeError('body'))
d3.callback('Ok3')


def callback(r):
    for s, v in r:
        if not s:
            print(v.getErrorMessage())

dl.addCallback(callback)