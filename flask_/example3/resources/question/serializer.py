from flask_restful import fields, marshal_with
from utils.serializer import BaseSerializer

class QuestionSerializer(BaseSerializer):
    text = fields.String

    # author = fields.Nested()
    #
    # comments = fields.Nested()
