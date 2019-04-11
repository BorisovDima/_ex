from select import select
import socket
from collections import deque

class server_generator:
    def __init__(self, port):
        self.tasks = deque()
        self.to_write = {}
        self.to_read = {}
        self.tasks.append(self.accept(port))

    def run(self):
        self.event_loop()

    def accept(self, port):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.bind(('0.0.0.0', port))
        sock.listen(5)
        while True:

            yield ('read', sock)
            conn, addr = sock.accept()

            self.tasks.append(self.do_client(conn))

########## corutine ########################################
    def do_client(self, client): # У каждого клиента свой генератор
        while True:

            yield ('read', client)
            data = client.recv(1024)

            if not data:
                break

            yield ('write', client)
            client.send(b'Echo=>%s' % data)

        client.close()
########################################################################


    def event_loop(self):
        while True:

            """
            Жду пока в одном из списков будет готов сокет
            """
            while not self.tasks:
                read, write, _ = select(self.to_read, self.to_write, []) # Жду новые задачи
                print(read, write, self.to_write, self.to_write)

                """
                Взял текущее состояние сокета 
                { socket: generator }
                """
                for sock in read:
                    self.tasks.append(self.to_read.pop(sock)) # ДОбавил задачу, очистил словарь (задача = генератор)
                for sock in write:
                    self.tasks.append(self.to_write.pop(sock))

            try:
                task = self.tasks.popleft()# Генератор
                event, sock = next(task) # возвращаю сокет текущего генератора

                # Сохраняю состояние сокета

                #жду его сообщения

                if event == 'read':
                    self.to_read[sock] = task

                #жду пока он будет готов принять мое сообщение

                elif event == 'write':
                    self.to_write[sock] = task

            except StopIteration:
                pass

server_generator(8002).run()