from core.route import Route
from .endpoints import Registration, Login, Logout

routes = Route()

routes.add_endpoint(path='/auth/registration', endpoint=Registration.get_endpoint())
routes.add_endpoint(path='/auth/login', endpoint=Login.get_endpoint())
routes.add_endpoint(path='/auth/logout', endpoint=Logout.get_endpoint())
