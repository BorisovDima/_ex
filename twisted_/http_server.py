from twisted_.internet import defer, reactor, task
from twisted_.web.resource import Resource, NoResource
from twisted_.web.server import Site, NOT_DONE_YET


class User(Resource):

    def __init__(self, name):
        self.name = name
        super().__init__()

    def render_GET(self, requset):
        return b'USER %s' % self.name



class Users(Resource):
    def getChild(self, name, request):
        print(name.isdigit())
        return NoResource() if not name.isdigit() else User(name)


class Handler(Resource):

    def getChild(self, path, request):
       return self if path in b' /' else super().getChild(path, request)


    def _wait(self, request):
        request.write(b'MAin')
        request.finish()


    def render_GET(self, request):
        task.deferLater(reactor, 4, self._wait, request)
        return NOT_DONE_YET

root = Handler()

root.putChild(b'user', Users())

factory = Site(root)
reactor.listenTCP(8000, factory)
reactor.run()