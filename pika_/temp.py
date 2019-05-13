
from twisted.internet import protocol
from twisted.application import internet
from twisted.application import service
from twisted.internet.defer import inlineCallbacks
from twisted.python import log

import pika
from pika.adapters import twisted_connection

PREFETCH_COUNT = 2


class PikaService(service.MultiService):
    name = 'amqp'

    def __init__(self, parameter):
        service.MultiService.__init__(self)
        self.parameters = parameter

    def startService(self):
        self.connect()
        service.MultiService.startService(self)

    def getFactory(self):
        return self.services[0].factory

    def connect(self):
        f = PikaFactory(self.parameters)
        serv = internet.TCPClient(
            host=self.parameters.host,
            port=self.parameters.port,
            factory=f)
        serv.setServiceParent(self)


class PikaProtocol(twisted_connection.TwistedProtocolConnection):

    def __init__(self, factory, parameters):
        super().__init__(parameters)
        self.factory = factory

    @inlineCallbacks
    def connectionReady(self):
        print('ok' * 100)


class PikaFactory(protocol.ReconnectingClientFactory):
    name = 'AMQP:Factory'

    def __init__(self, parameters):
        self.parameters = parameters
        self.client = None
        self.queued_messages = []
        self.read_list = []

    def buildProtocol(self, addr):
        self.resetDelay()
        log.msg('Connected', system=self.name)
        self.client = PikaProtocol(self, self.parameters)
        return self.client



application = service.Application("pikaapplication")

ps = PikaService(pika.ConnectionParameters())

ps.setServiceParent(application)
