from sqlalchemy import create_engine


engine = create_engine('mysql+mysqlconnector://root:1488@localhost:3306/test')


try:
    engine.execute('CREATE TABLE test_index( '
                   'id INT PRIMARY KEY AUTO_INCREMENT, '
                   'name VARCHAR(100), '
                   'age INT, '
                   'family VARCHAR(100), '
                   'INDEX(name, age), '
                   'INDEX(family))')
except Exception as e:
    print(e)

