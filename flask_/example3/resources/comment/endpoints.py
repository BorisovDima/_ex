from flask_restful import Resource
from .models import Comment

class CommentView(Resource):

    def get(self):
        return {'hello': 'HeEEEE'}

    def post(self):
        return {'hello': 'HeEEEE'}

    def put(self):
        return {'hello': 'HeEEEE'}

    def delete(self):
        return {'hello': 'HeEEEE'}


class CommentViewList(Resource):

    def get(self):
        return {'hello': 'HeEEEE'}
