from twisted.protocols.basic import LineReceiver
from twisted.internet.protocol import Factory
from twisted.internet import reactor
from twisted.application import service, internet


class TestProto(LineReceiver):

    def dataReceived(self, data):
        print(data)





f = Factory()
f.protocol = TestProto


application = service.Application('application')

service_ = internet.TCPServer(8000, f)
service_.setServiceParent(application)