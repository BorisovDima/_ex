import socket
from select import select
import sys

class selectsocket:

    def __init__(self, addr):
        self.monitor_files = []
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.bind(('0.0.0.0', addr))
        self.server.listen(5)
        self.monitor_files.append(self.server)
        self.write = []
        self.event_loop()
        self.server.close()

    def accept(self, server):
        conn, addr = server.accept()
        self.monitor_files.append(conn)
        # self.write.append(conn)

#Select - мониторит изменения тех файловых обьектов, которые мы в нее передали. На вход функция select получает три списка
# С файловыми дескрипторами или с обьектами у которых есть метод fileno (File Object). Первый список те обьекты за которыми
# нужно наблюдать когда они станут доступны для чтения, второй список ,,, когда они станут доступны для записи
# третий список - это обьеткы где мы ожидаем ошибки

    def event_loop(self):
        while True:
            ready, write, _ = select(self.monitor_files, self.write, [])
            print(ready, write)
            for sock in ready:
                self.accept(sock) if sock is self.server else self.send(sock)


    def send(self, client):
            msg = client.recv(1024)
            if msg:
                print(msg)
                msg = b'Echo=> (%s)' % msg
                client.send(msg)
            else:
                client.close()
                del self.monitor_files[self.monitor_files.index(client)]

addr = 8009
if __name__ == '__main__':
    selectsocket(addr)