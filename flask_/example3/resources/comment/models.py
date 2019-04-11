from utils.models import BaseModel
from app import db


class Comment(BaseModel):
    text = db.Column(db.String(224))
    author_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    question_id = db.Column(db.Integer, db.ForeignKey('question.id', ondelete='CASCADE'))