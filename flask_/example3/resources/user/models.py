from utils.models import BaseModel
from app import db

class User(BaseModel):
    username = db.Column(db.String(124), unique=True, nullable=False)
    password = db.Column(db.String(124), nullable=False)

    questions = db.relationship('Question', backref='author', lazy='dynamic')
    comments = db.relationship('Comment', backref='author', lazy='dynamic')

