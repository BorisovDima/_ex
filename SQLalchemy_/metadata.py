"""
Для описания структуры базы данных используют 3 основных класса:

    sqlalchemy.schema.Table - таблица
    sqlalchemy.schema.Column - поле таблицы
    sqlalchemy.schema.MetaData - список таблиц

"""

from sqlalchemy import Table, MetaData, Column, Integer, String, create_engine, ForeignKey


engine = create_engine('postgresql+psycopg2://test_alchemy:19960213@localhost/sqlalshemy_test')
metadata = MetaData(bind=engine) # Вся информация о таблицах базы данных складывается в объект класса sqlalchemy.schema.MetaData

my_table = Table('my_table',metadata,
                 Column('id', Integer, primary_key=True),
                 Column('name', String)
                 )


my_table_drop = Table('my_table_drop', metadata,
                 Column('id', Integer, primary_key=True),
                 Column('name', String)
                 )


metadata.create_all()
my_table_drop.drop() # delete
my_table_drop.create() # create

#print(my_table.select(''))



##################### foreing key ########################################

one_to_many = Table('one_to_many', metadata,
                 Column('id', Integer, primary_key=True),
                 Column('name', String, index=True),
                 Column('foreign', Integer, ForeignKey('many_to_one.id'))
                 )

many_to_one = Table('many_to_one', metadata,
                 Column('id', Integer, primary_key=True),
                 Column('name', String),
                 )


metadata.create_all()

res = engine.execute(many_to_one.select())
res2 = engine.execute(one_to_many.select())


print(res.fetchall())
print(res2.fetchall())

conn = engine.connect()

#tranc = conn.begin()
#conn.execute(many_to_one.insert().values(id=14, name='ONe1'))
#tranc.commit()

#engine.execute(many_to_one.insert().values(id=1, name='ONE'))
# engine.execute(one_to_many.insert().values(name='first', id=1, foreign=1))


############################## load shema ##############################


"""
В SQLAlchemy рефлексия означает автоматическую загрузку схемы таблицы из уже существующей базы данных
"""
metadata2 = MetaData()

user_reflected = Table('my_user', metadata2, autoload=True, autoload_with=engine)

metadata2.reflect(bind=engine) # Загрузка схем всех таблиц из DB engine

for table in metadata2.tables:
    print(table)

################################   inspect ####################################

from sqlalchemy import inspect

inspector = inspect(engine)

print(inspector.get_table_names())
