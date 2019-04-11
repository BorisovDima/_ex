from flask_ import Blueprint
from flask_restful import Api
from .endpoints import QuestionView, QuestionViewList


question = Blueprint('question', __name__)
api = Api(question)


api.add_resource(QuestionViewList, '/') # list - Get
api.add_resource(QuestionView, '/<id>/') #
