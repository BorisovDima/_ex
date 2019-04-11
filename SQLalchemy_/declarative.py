from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

############## main ###################
engine = create_engine('postgresql+psycopg2://test_alchemy:19960213@localhost/sqlalshemy_test')
base = declarative_base(bind=engine)
####################################


class tablename:
    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__()
        cls.__tablename__ = cls.__name__.lower()

#####################  tables ################################
class DeclTable(tablename, base):

    id = Column(Integer, primary_key=True)
    name = Column(String)

    def __repr__(self):
        return str(self.id)

print(DeclTable.__table__) # Для каждого класса унаследованного от базового автоматически создается схема таблицы
################################################

print(base.metadata.tables, '_____')
base.metadata.create_all()

########################## session ####################################
from sqlalchemy.orm import Session
import random

session = Session(bind=engine)
# row = DeclTable(id=2, name='Bor' )
# session.add(row)
# session.commit()
print(session.query(DeclTable, DeclTable).filter_by(id=2).first(), '')


from sqlalchemy.orm import sessionmaker

Session = sessionmaker()
session = Session(bind=engine)

row = DeclTable(id=random.randrange(1000), name='Bor' )
session.add(row)
session.commit()

####################################################
query = session.query(DeclTable)
print(type(query))
row = query.first()
print(row.name)

############################ Foreing key ########################


class Many(tablename, base):
    id = Column(Integer, primary_key=True)
    name = Column(String(60))
    many_id = Column(Integer, ForeignKey('one.id'))
    one = relationship('One', backref='many')

    def __repr__(self):
        return str(self.id) + ' One'

class One(tablename, base):
    id = Column(Integer, primary_key=True)
    name = Column(String(60))

    def __repr__(self):
        return 'relation on %s' % self.id

base.metadata.create_all()

# many = Many(id=1, name='many1')
# one = One(id=1, name='one1', many=many)
# session.add_all([many, one])
# session.commit()



one = session.query(One).filter_by(id=1)
one = one.first()

print(one.many)

two = session.query(Many).filter_by(id=1)
two = two.first()
print(two.one)

# two.one = [One(id=12, name='test'), One(id=13, name='test')]
#
# session.add(two)
# session.commit()



#########################



print(session.query(Many, One).filter(Many.id == One.id).first())
print(session.query(Many, One).join(One).all())
print(session.query(Many, One).join(One, One.id == Many.id).all())

print(session.query(One).filter(One.id.in_([1,2,3])).all())


#############################################

Many.one.property.cascade = "all, delete, delete-orphan"

# one = One(id=111, name='HI')
# one1 = One(id=112, name='HI1')
# one2 = One(id=113, name='HI2')
#
# many = Many(id=1488, name='I del')
#
# many.one = [
#     one,
#     one1,
#     one2
# ]
#

two = session.query(Many).filter_by(id=1488).first()
one = session.query(One).filter_by(id=111)
print(one.first(), two)
del two
session.commit()
print(one.first())

LikeQuerySet = session.query(One)
LikeQuerySet = LikeQuerySet.filter(One.id.in_([2,2,3]))

LikeQuerySet = LikeQuerySet.filter(One.id==1)

print(LikeQuerySet.all())



