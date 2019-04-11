from app import db
from utils.models import BaseModel


class Question(BaseModel):
    text = db.Column(db.String(524))
    author_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    comments = db.relationship('Comment', backref='question', lazy='dynamic',  passive_deletes=True)