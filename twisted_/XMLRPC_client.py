from xmlrpc.client import ServerProxy

server = ServerProxy('http://127.0.0.1:8103/') # big_mixin_example.py
print(server.test(1))
