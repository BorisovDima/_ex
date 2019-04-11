from flask_restful import fields, marshal_with
from utils.serializer import BaseSerializer

class UserSerializer(BaseSerializer):
    username = fields.String

    # questions = fields.Nested()
    #
    # comments = fields.Nested()
