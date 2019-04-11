from sqlalchemy import create_engine, MetaData, Column, String, Integer, ForeignKey
from sqlalchemy.orm import Session, relationship
from sqlalchemy.ext.declarative import declarative_base

# e = create_engine('mysql+mysqlconnector://root:1488@localhost:3306/test')
# ses = Session(bind=e)
#
# meta = MetaData()
#
# meta.reflect(bind=e)
#
#
# from sqlalchemy.ext.serializer import dumps
#
# print(dumps(ses.query(meta.tables['Category'])))



engine = create_engine('postgresql+psycopg2://test_alchemy:19960213@localhost/sqlalshemy_test')
base = declarative_base(bind=engine)

class DeclTable(base):
    __tablename__ = 'testim'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    child = relationship('DeclTableChild', backref='parent', lazy='dynamic')

    def __repr__(self):
        return str(self.id)

class DeclTableChild(base):
    __tablename__ = 'testim_child'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    parent_id = Column(Integer, ForeignKey('testim.id'))

    def __repr__(self):
        return str(self.id)


base.metadata.create_all()
session = Session(bind=engine)

u = session.query(DeclTable).get(4)


# session.add(u)

# session.add(c)
# session.commit()


print(u.__mapper__.relationships.keys())
print(u.__table__.columns.keys())

print(getattr(u, 'child')[:0])