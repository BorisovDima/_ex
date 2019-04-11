from sqlalchemy import create_engine
import random


engine = create_engine('postgresql+psycopg2://test_alchemy:19960213@localhost/sqlalshemy_test')


try:
    engine.execute('CREATE TABLE my_user ('
                   'test_id integer primary key UNIQUE,'
                   'name varchar)')                   #  execute with commit 
except Exception:
    pass


# engine.execute('insert into my_user(test_id, name) values (2, 10)')
result = engine.execute('select * from my_user')


for i in result:
    print(i)



################# transaction #######################

conn = engine.connect()

trans = conn.begin()
conn.execute("insert into my_user(test_id, name) values (%s, 'h1')" % random.randrange(1000))
trans.commit()
# conn.close()





