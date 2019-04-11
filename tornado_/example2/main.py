from tornado.httpserver import HTTPServer
from tornado.ioloop import IOLoop
from tornado.options import options

from app import ChatApp






if __name__ == '__main__':
    app = ChatApp()
    server = HTTPServer(app)
    server.listen(options.PORT)
    IOLoop.current().start()

