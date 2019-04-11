from core.route import Route
from .endpoints import SendMessage

routes = Route()

routes.add_endpoint(path='/chat/dddd', endpoint=SendMessage.get_endpoint())
