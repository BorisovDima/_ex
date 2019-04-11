from flask_ import Blueprint
from flask_restful import Api
from .endpoints import CommentView, CommentViewList


comment = Blueprint('comment', __name__)
api = Api(comment)


api.add_resource(CommentViewList, '/') # list - Get
api.add_resource(CommentView, '/<id>/') #

