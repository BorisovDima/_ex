from sqlalchemy import ForeignKey, Column, Integer, String, Table
from sqlalchemy.orm import relationship, backref

from core.models import BaseChatModel, Media


user_room = Table('user_room', BaseChatModel.metadata,
                  Column('user_id', Integer, ForeignKey('user.id')),
                  Column('room_id', Integer, ForeignKey('room.id'))
                  )


class Room(BaseChatModel, Media(1)):
    __tablename__ = 'room'

    messages = relationship('Message', backref='room', lazy='dynamic',  passive_deletes=True)

    author_id = Column(Integer, ForeignKey('user.id'))
    users = relationship('User', secondary=user_room, backref=backref('rooms', lazy='dynamic'))

    def get_absolute_url(self):
        pass



class Message(BaseChatModel, Media(3)):
    __tablename__ = 'message'

    text = Column(String(500),  nullable=False)
    room_id = Column(Integer, ForeignKey('room.id', ondelete='CASCADE'))
    author_id = Column(Integer, ForeignKey('user.id'))

    def get_absolute_url(self):
        pass

