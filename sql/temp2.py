from sqlalchemy import create_engine


engine = create_engine('mysql+mysqlconnector://root:1488@localhost:3306/test')

try:
    engine.execute('CREATE TABLE IF NOT EXISTS coom('
               'id INT PRIMARY KEY'
               'name VARCHAR(124))')
except:
    pass


with engine.begin() as conn:
    conn.execute("INSERT INTO coom(name) values('Conn')")



