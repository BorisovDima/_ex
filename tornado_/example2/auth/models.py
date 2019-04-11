from sqlalchemy import ForeignKey, Column, Integer, String, Boolean, DateTime, Text, Time
from sqlalchemy.orm import relationship

from core.models import BaseChatModel, Media
from core.serializer import SimpleSerializer

from datetime import datetime


class User(SimpleSerializer, BaseChatModel, Media(1)):
    __tablename__ = 'user'
    serialize_fields = ['username', 'about_me', 'last_activity']

    password = Column(String(66), nullable=False)
    username = Column(String(50), nullable=False)
    about_me = Column(String(124))
    last_activity = Column(DateTime, default=datetime.utcnow)
    messages = relationship('Message', backref='author', lazy='dynamic')
    created_rooms = relationship('Room', backref='author', lazy='dynamic')

    is_staff = Column(Boolean, default=False)
    is_superuser = Column(Boolean, default=False)

    def get_absolute_url(self):
        pass

    def set_password(self, password):
        pass


class JWTtoken(BaseChatModel):
    __tablename__ = 'token'

    user_id = Column(Integer, ForeignKey('user.id'), nullable=False)
    token = Column(Text, nullable=False)
    expired = Column(Time, nullable=False)
