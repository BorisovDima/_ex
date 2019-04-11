from zope.interface import Interface, implementer
from twisted_.python import components


class IAmericanSocket(Interface):

    def voltage():
        """
        Return the voltage
        """


class IUKSocket(Interface):

    def voltage():
        """
        Return the voltage
        """


@implementer(IAmericanSocket)
class AmericanSocket:
    def voltage(self):
        return 120

@implementer(IUKSocket)
class UKSocket:
    def voltage(self):
        return 240



@implementer(IAmericanSocket) # Adapter
class AdaptToAmericanSocket:
    def __init__(self, original):
        self.original = original

    def voltage(self):
        return self.original.voltage() / 2



components.registerAdapter(AdaptToAmericanSocket, IUKSocket, IAmericanSocket) # Adapter, Adapt from, Adapt to *

print(IAmericanSocket(UKSocket())) # adapter
print(IAmericanSocket(AmericanSocket())) # the same


def check_socket(socket):
    socket = IAmericanSocket(socket)
    if socket.voltage() == 120:
        print('NicE!')

check_socket(UKSocket())
check_socket(AmericanSocket())

