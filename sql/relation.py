import sqlite3

engine = sqlite3.connect('relations')

engine.execute("PRAGMA foreign_keys=ON")
cursor = engine.cursor()

# One
engine.execute("""
CREATE TABLE IF NOT EXISTS families (
     id INTEGER PRIMARY KEY,
     name TEXT NOT NULL);
     """)

#  Many
engine.execute("""
     CREATE TABLE IF NOT EXISTS  articles (
    id INTEGER PRIMARY KEY,
    name VARCHAR(32) NOT NULL,
    family_id INTEGER,
    FOREIGN KEY(family_id) REFERENCES families(id));   
     """)

cursor.execute('INSERT INTO families(name) values (?)', ('one to many',))
cursor.execute('INSERT INTO articles(name, family_id) values (?, ?)', ('many to one', cursor.lastrowid))
engine.commit()
print(cursor.execute('SELECT a.name, a.id, f.name, f.id FROM articles a '
                     'JOIN families f '
                     'ON a.family_id = f.id').fetchall())

####################################################################

# One
engine.execute("""
CREATE TABLE IF NOT EXISTS families2 (
     id INTEGER PRIMARY KEY,
     name TEXT NOT NULL,
     article_id INTEGER,
     FOREIGN KEY(article_id) REFERENCES articles2(id));
     """)
# One
engine.execute("""
     CREATE TABLE IF NOT EXISTS  articles2 (
    id INTEGER PRIMARY KEY,
    name VARCHAR(32) NOT NULL,
    family_id INTEGER,
    FOREIGN KEY(family_id) REFERENCES families2(id));   
     """)


#####################################################################

# Many
engine.execute("""
CREATE TABLE IF NOT EXISTS families3 (
     id INTEGER PRIMARY KEY,
     name TEXT NOT NULL);
     """)

# Many
engine.execute("""
     CREATE TABLE IF NOT EXISTS  articles3(
            id INTEGER PRIMARY KEY,
            name VARCHAR(32) NOT NULL
    );  
     """)


# Through
engine.execute("""
CREATE TABLE IF NOT EXISTS articles_families (
        article_id INTEGER,
        family_id INTEGER,
        FOREIGN KEY(article_id) REFERENCES articles(id),
        FOREIGN KEY(family_id) REFERENCES families(id));
        """)

cursor.execute('INSERT INTO families3(name) values (?)', ('one to many families3',))
cursor.execute('INSERT INTO articles3(name) values (?)', ('one to many articles3',))
cursor.execute('INSERT INTO articles_families(article_id, family_id) values (?, ?)', (1,1))
print(cursor.execute("""
                    SELECT f.name, a.name FROM articles_families af
                        JOIN families3 f ON f.id = af.family_id
                        JOIN articles3 a ON a.id = af.article_id
                    """).fetchall())
engine.commit()


###################################

# One
cursor.execute("""
CREATE TABLE IF NOT EXISTS families5 (
     id INTEGER PRIMARY KEY,
     name TEXT NOT NULL);
     """)

#  Many
cursor.execute("""
     CREATE TABLE IF NOT EXISTS  articles5 (
    id INTEGER PRIMARY KEY,
    name VARCHAR(32) NOT NULL,
    family_id INTEGER,
    FOREIGN KEY(family_id) REFERENCES families5(id) ON DELETE CASCADE);   
     """)

cursor.execute('INSERT INTO families5(name) values (?)', ('one to many',))
cursor.execute('INSERT INTO articles5(name, family_id) values (?, ?)', ('many to one', cursor.lastrowid))
print(cursor.execute('SELECT * FROM families5').fetchall())
print(cursor.execute('SELECT * FROM articles5').fetchall())
cursor.execute('DELETE FROM families5')

print(cursor.execute('SELECT * FROM families5').fetchall())
print(cursor.execute('SELECT * FROM articles5').fetchall())

engine.commit()