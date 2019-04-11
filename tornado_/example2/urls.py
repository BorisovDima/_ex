from core.route import Route

from chat.urls import routes as chat_route
from auth.urls import routes as auth_route

routes = Route()

routes.add_endpoint(path='/chat/', endpoint=chat_route)
routes.add_endpoint(path='/auth/', endpoint=auth_route)

