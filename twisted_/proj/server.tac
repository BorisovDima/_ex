import sys, os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))


from twisted.application import internet, service
from service import EchoFactory

application = service.Application('Test')
serv = internet.TCPServer(8000, EchoFactory())
serv.setServiceParent(application)