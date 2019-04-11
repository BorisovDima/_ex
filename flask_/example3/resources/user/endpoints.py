from flask_restful import Resource
from .models import User


class BaseUserView(Resource):
    def post(self): # create
        return {'hello': 'HeEEEE'}

    def get(self): # list
        pass

class LoginUserView(Resource):
    def post(self):
        pass

class LogoutUserView(Resource):
    def post(self):
        pass


class DetailUserView(Resource):
    def get(self): # retrieve
        return {'hello': 'HeEEEE'}



