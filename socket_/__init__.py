import threading
import socket
# def server():
#     s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#     s.bind(('0.0.0.0', 8009))
#     s.listen(10)
#     print('Wait')
#     c, a = s.accept()
#     print('Tuta')
#     c.setblocking(False)
#     print(repr(c.recv(1024)))
#     print('Pass')
#     while True:
#         try:
#             print(c.recv(1024))
#         except Exception as i:
#             print(i)
#         else:
#             break
#
# threading.Thread(target=server).start()
# import time
# time.sleep(2)
# s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# s.connect(('0.0.0.0', 8009))
# print(repr(s.recv(1024)))
# s.send(b'HI')
# time.sleep(0.2)
# s.send(b'HI!')

