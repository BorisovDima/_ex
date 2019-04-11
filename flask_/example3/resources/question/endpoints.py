from flask_restful import Resource
from .models import Question


class QuestionView(Resource):

    def get(self):
        return {'hello': 'HeEEEE'}

    def post(self):
        return {'hello': 'HeEEEE'}

    def put(self):
        return {'hello': 'HeEEEE'}

    def delete(self):
        return {'hello': 'HeEEEE'}




class QuestionViewList(Resource):

    def get(self):
        return {'hello': 'HeEEEE'}
