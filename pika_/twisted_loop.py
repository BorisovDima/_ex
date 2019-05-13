import pika
from twisted.internet.protocol import ReconnectingClientFactory, Factory
from twisted.internet import reactor, defer, protocol
from pika.adapters import twisted_connection
from twisted.application import service, internet



class PikaProtocol(twisted_connection.TwistedProtocolConnection):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    @defer.inlineCallbacks
    def connectionReady(self):
        self.ch = yield self.channel()
        yield self.start_mq()


    @defer.inlineCallbacks
    def start_mq(self, exchange='test'):
        yield self.ch.exchange_declare(exchange=exchange, exchange_type='fanout')
        r = yield self.ch.queue_declare('twisted', durable=True)
        yield self.ch.queue_bind(exchange=exchange, queue=r.method.queue, routing_key='')
        yield self.start_consume(r.method.queue)
        self.connected = True

    @defer.inlineCallbacks
    def start_consume(self, queue):
        print('TUTA')
        queue, consume_tag = yield self.ch.basic_consume(queue=queue,
                                                         auto_ack=True)
        print(queue, consume_tag)
        d = queue.get()
        d.addCallback(lambda r: self.resive_msgs(queue, self.callback, *r))

    def resive_msgs(self, queue, callback, ch, method, properties, body):
        print(f'Echo{body}')
        callback(body)
        d = queue.get()
        d.addCallback(lambda r: self.resive_msgs(queue, callback, *r))

    @defer.inlineCallbacks
    def sendMessage(self, msg, exchange='test'):
        if self.connected:
            yield self.ch.basic_publish(exchange=exchange,
                                        routing_key='',
                                        body=msg.decode())



class PikaFactory(ReconnectingClientFactory):
    client = None

    def __init__(self, parameters):
        self.params = parameters

    def buildProtocol(self, addr):
        self.client = PikaProtocol(parameters=self.params)
        return self.client

    def put(self, data):
        self.client.sendMessage(data)

    def get(self):
        pass

#########################################################

class TestProtocol(protocol.Protocol):
    def __init__(self, f):
        self.factory = f

    def dataReceived(self, data):
        rmq = self.factory.rmq
        print(self.transport)
        rmq.client.callback = self.transport.write
        rmq.put(data)

class TestFactory(Factory):
    def __init__(self, rmq_f):
        self.rmq = rmq_f

    def buildProtocol(self, addr):
        protocol = TestProtocol(self)
        return protocol

class TestService(service.Service):
    def __init__(self, rmq):
        self.rmq = rmq
        super().__init__()

    def startService(self):
        factory = TestFactory(self.rmq)
        self.server = reactor.listenTCP(8000, factory)

    def stopService(self):
        self.server.stopListening()


params = pika.ConnectionParameters('localhost', port=5672)

application = service.Application('Pika-pika')

factory = PikaFactory(parameters=params)
rmq_client = internet.TCPClient(host=params.host,
                                port=params.port,
                                factory=factory)

test_service = TestService(factory)

rmq_client.setServiceParent(application)
test_service.setServiceParent(application)

