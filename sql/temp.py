from sqlalchemy import create_engine


engine = create_engine('mysql+mysqlconnector://root:1488@localhost:3306/test')


# One
engine.execute("""
CREATE TABLE IF NOT EXISTS families5 (
     id INTEGER PRIMARY KEY,
     name TEXT NOT NULL);
     """)

#  Many
engine.execute("""
     CREATE TABLE IF NOT EXISTS  articles5 (
    id INTEGER PRIMARY KEY,
    name VARCHAR(32) NOT NULL,
    family_id INTEGER,
    FOREIGN KEY(family_id) REFERENCES families5(id) ON DELETE CASCADE);   
     """)

