from twisted_.internet import reactor, protocol
from twisted_.protocols import basic
from twisted_.internet.endpoints import TCP4ServerEndpoint, connectProtocol

class Greater(basic.LineReceiver):
    def lineReceived(self, line):
        print(line)
        self.transport.write(line)

class Fac(protocol.Factory):
    protocol=Greater


point = TCP4ServerEndpoint(reactor, 8001)
point.listen(Fac())
reactor.run()