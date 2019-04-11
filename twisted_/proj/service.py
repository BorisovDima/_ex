from twisted_.internet import protocol

class EchoProtocol(protocol.Protocol):

    def dataReceived(self, data):
        print(data)
        self.transport.write(data)


class EchoFactory(protocol.Factory):
    def buildProtocol(self, addr):
        print(addr)
        return EchoProtocol()


