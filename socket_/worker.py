import os
import socket
import threading
import multiprocessing



def client_request(client):
    with client as client:
        while True:
            data = client.recv(1024)
            if not data:
                break
            data = b'Echo =>%s' % data
            client.sendall(data)



class Worker(multiprocessing.Process):
    def __init__(self, server):
        super().__init__()
        self.server = server

    def run(self):
        sock = self.server # В каждом процессе тот же самый сокет (скопировали всю инфу из родительского)
        threads = []
        while True:
            print(os.getpid())
            # Системный вызов accept распределит равномерно между всеми дочерними процессами новые входящие соединения
            # Когда все доч. процессы делают системный вызов accept то по умолчанию они спят, но если пришло новое соединение
            # то операционная система разбудит их все, и это затрачивает много ресурсов
            conn, addr = sock.accept()
            print(addr)
            t = threading.Thread(target=client_request, args=(conn,))
            t.start()
            threads.append(t)
            print(threads)
        for th in threads:
            th.join()


def server(count=5):
    workers = []
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
        server.bind(('0.0.0.0', 8006))
        server.listen(10)
        for i in range(count):
            w = Worker(server)
            w.start()
            workers.append(w)

        for i in workers:
            i.join()


server()
