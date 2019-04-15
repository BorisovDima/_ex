from __future__ import print_function
import os
from socket import SOL_SOCKET, socketpair
from struct import unpack, pack
from twisted.python.sendmsg import SCM_RIGHTS, sendmsg, recvmsg
import multiprocessing


# Copying File Descriptors


class SubProcess(multiprocessing.Process):

    def __init__(self, sock, *args, **kwargs):
        self.sock = sock
        super().__init__(*args, **kwargs)

    def run(self):
        r, w = os.pipe()
        r = pack('i', r)
        sendmsg(socket=self.sock, data=b'b', ancillary=[(SOL_SOCKET, SCM_RIGHTS, r)])
        os.write(w, b'Hello')




def fd_from_unix():
    c, p = socketpair()
    SubProcess(c).start()
    data, an, f = recvmsg(p, 1024)
    r_copy = unpack('i', an[0][2])[0]
    print(r_copy)
    print(os.read(r_copy, 1024))

fd_from_unix()


# Copying File Descriptors

import threading
import time
import socket

def server():
    sock = socket.socket(socket.AF_UNIX)
    if os.path.exists('unix_sock'):
        os.remove('unix_sock')
    sock.bind('unix_sock')
    sock.listen(11)
    conn, addr = sock.accept()
    r, w = os.pipe()
    sendmsg(conn, b'0', [(SOL_SOCKET, SCM_RIGHTS, pack('i', r))])
    os.write(w, b'HYYYYY!')

threading.Thread(target=server).start()
time.sleep(2)
cl = socket.socket(socket.AF_UNIX)
cl.connect('unix_sock')
d, an, f = recvmsg(cl, 1024)
r_copy = unpack('i', an[0][2])[0]
print(os.read(r_copy, 1024))


