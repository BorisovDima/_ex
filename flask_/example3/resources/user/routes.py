from flask_ import Blueprint
from flask_restful import Api
from .endpoints import BaseUserView, DetailUserView, LoginUserView, LogoutUserView

user = Blueprint('user', __name__)
api = Api(user)


api.add_resource(BaseUserView, '/') # create - list
api.add_resource(LoginUserView, '/logout/') #
api.add_resource(LogoutUserView, '/logout/') #
api.add_resource(DetailUserView, '/<id>/') #  retrieve

