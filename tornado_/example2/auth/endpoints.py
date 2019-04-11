from core.endpoints import BaseEndpoint

from .backend import SimpleJWT
from .models import User
from tornado_sqlalchemy import SessionMixin, as_future

class Registration(SimpleJWT, SessionMixin, BaseEndpoint):

    async def post(self, request, args, body):
        username, password = body['username'], body['password']
        new_user = User(username=username)
        new_user.set_password(password)
        await new_user.save(self.session)
        return new_user.serialize()



class Login(SimpleJWT, SessionMixin,  BaseEndpoint):

    def create_token(self, username, password):
        payload = {
            'exp': 1200,
            'username': username
        }
        token = self.generate_token(payload)

    def post(self, request, *args, **kwargs):
        username, password = request
        user = self.session.query(User).filter_by(username=username).first()
        if user:
            token = self.create_token(username, password)
        else:
            token = None
        return token

class Logout(SimpleJWT, BaseEndpoint):
    pass