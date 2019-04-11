from flask_restful import fields, marshal_with
from utils.serializer import BaseSerializer

class CommentSerializer(BaseSerializer):
    text = fields.String

    # author = fields.Nested()
    #
    # question = fields.Nested()

