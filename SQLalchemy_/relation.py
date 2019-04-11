
from sqlalchemy import Table, MetaData, Column, Integer, String, create_engine, ForeignKey
from sqlalchemy.orm import relationship, backref
from sqlalchemy.ext import declarative

engine = create_engine('postgresql+psycopg2://test_alchemy:19960213@localhost/sqlalshemy_test')

BaseChatModel = declarative.declarative_base(bind=engine)


user_room = Table('user_room', BaseChatModel.metadata,
                  Column('user_id', Integer, ForeignKey('user.id')),
                  Column('room_id', Integer, ForeignKey('room.id'))
                  )



class Room(BaseChatModel):
    __tablename__ = 'room'
    id = Column(Integer, primary_key=True)
    users = relationship('User', secondary=user_room, lazy='dynamic', backref=backref('rooms', lazy='dynamic'))

    def get_absolute_url(self):
        pass



class User(BaseChatModel):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    text = Column(String(500),  nullable=False)


    def get_absolute_url(self):
        pass

BaseChatModel.metadata.create_all()
from sqlalchemy.orm import Session
session = Session()
print(session.query(User).all())
m = User(text='12212', rooms=[Room()])
session.add(m)
session.commit()
print(m.rooms.all(), 'dddddddddddddddddddddddd')
u = session.query(User).get(1)
print(u.text)
u.text = 'NEW TEXT'
session.commit()
u = session.query(User).get(1)
print(u.rooms.all())

room = Room()
session.add(room)
session.commit()

print(u.rooms)
u.rooms = [room, room, room]

session.commit()

print(room.users.all())
print(type(room.users))