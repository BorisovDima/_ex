from tornado.websocket import WebSocketHandler, WebSocketClosedError
from .utils import parse_message
from .route import Route


class BaseHandler(WebSocketHandler):

    routes = Route() # default

    async def open(self, *args, **kwargs):
        print('Open!')

    def resolve_endpoint(self, url):
        endpoint = self.routes.resolve(url)
        return endpoint


    def _send(self, response):
        """ send message to client: kwargs - json or dict"""
        try:
            self.write_message(response)
        except WebSocketClosedError as e:
            # logger.error('WebSocket closed error %s: client %s' % (self, e))
            self.close()


    async def on_message(self, message):
        id, method, url, args, body = parse_message(message)
        endpoint = self.resolve_endpoint(url)
        response = await self.execute(endpoint, method, args, body)
        self._send(response)


    async def execute(self, endpoint, method, args, body):
        return endpoint.dispatch(method, self.request, args, body)

    def on_close(self):
        pass

