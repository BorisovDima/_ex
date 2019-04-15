from twisted.internet.protocol import DatagramProtocol
from twisted.internet import reactor


class UDP(DatagramProtocol):
    def stopProtocol(self):
        print('END')

    def startProtocol(self):
        print(self.transport)
        print('Start')


    def datagramReceived(self, datagram, addr):
        print(datagram, addr)
        addr[1]
        self.transport.write(b'%s - %s' % (datagram, str(addr).encode()), addr)

d = reactor.resolve('google.com')
d.addCallback(lambda r: print(r))

# reactor.listenUDP(8001, UDP())
# reactor.run()

################## my socket
import socket
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(('0.0.0.0', 8000))

s.setblocking(False)
# reactor.adoptDatagramPort(s.fileno(), socket.AF_INET, UDP())
# reactor.run()

################## MULTICAST

class MultiUDP(DatagramProtocol):

    def startProtocol(self):
        self.transport.setTTL(5)
        self.transport.joinGroup("228.0.0.5")

    def datagramReceived(self, datagram, addr):
        print(datagram, addr)
        self.transport.write(b"Server: Pong", addr)

reactor.listenMulticast(9999, MultiUDP(), listenMultiple=True)
reactor.run()
