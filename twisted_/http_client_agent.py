from twisted_.web.client import Agent, readBody
from twisted_.internet import protocol, reactor, defer

class AgentProtocol(protocol.Protocol):
    def __init__(self, d):
        self.d = d
        super().__init__()

    def dataReceived(self, data):
        print(data)

    def connectionLost(self, r):
        print(r)
        # self.d.callback(None)

def callback(res):
    res.deliverBody(AgentProtocol(d))
    for h, v in res.headers.getAllRawHeaders():
        print(h, v)

def error(err):
    print(err)


agent = Agent(reactor)
d = agent.request(b'GET', b'http://www.google.com/')
d.addCallbacks(callback, error)
d.addBoth(lambda arg: reactor.stop())
reactor.run()


