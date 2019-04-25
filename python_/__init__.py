import pack

print(pack.ts)

import socket
import threading


def server():
    s = socket.socket()
    s.bind(('0.0.0.0', 1202))
    s.listen(4)
    print(s.accept())



threading.Thread(target=server).start()
import time
time.sleep(2)
with socket.create_connection(('192.168.43.131', 1202)):
    print('d')