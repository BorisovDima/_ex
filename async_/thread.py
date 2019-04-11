import threading
import time
import socket

def accept():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
        server.bind(('0.0.0.0', 8000))
        server.listen(5)
        while True:
            conn, addr = server.accept()
            threading.Thread(target=send, args=(conn,)).start()


def send(client):
    msg = client.recv(1024)
    msg = b'Echo=> (%s)' % msg
    client.sendall(msg)
    print('Close!')

accept()

#
# ####################### very bad ######################
# def started():
#     time.sleep(1)
#     for count in reversed(range(1, 4)):
#         time.sleep(1)
#         print('%d...' % count)
#     print('Rocket launced!')
#
#
# threads = []
# for _ in range(1000):
#     thread = threading.Thread(target=started, args=())
#     thread.start()
#     threads.append(thread)
# for thread in threads:
#     thread.join()
# print('END')