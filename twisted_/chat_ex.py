from twisted_.internet import protocol, reactor


class ChatProtocol(protocol.Protocol):  # Stateless - one client one instance

    def connectionMade(self):
        self.factory.count_users += 1
        self.factory.users.append(self)


    def dataReceived(self, data):
        msg = data.strip()
        self.broadcast_msg(msg)


    def broadcast_msg(self, msg):
        for u in self.factory.users:
            if u != self:
                u.transport.write(msg)


class ChatFactory(protocol.Factory): # Persistent
    users = []
    count_users = 0
    protocol = ChatProtocol

reactor.listenTCP(8000, ChatFactory())
reactor.run()


