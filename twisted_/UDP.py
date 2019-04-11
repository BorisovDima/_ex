from twisted_.internet.protocol import DatagramProtocol
from twisted_.internet import reactor


class UDP(DatagramProtocol):

    def datagramReceived(self, datagram, addr):
        print(datagram, addr)
        self.transport.write(b'%s - %s' % (datagram, str(addr).encode()), addr)

d = reactor.resolve('google.com')
d.addCallback(lambda r: print(r))
reactor.listenUDP(8000, UDP())
reactor.run()