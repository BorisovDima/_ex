from sqlalchemy import create_engine

e = create_engine('mysql+mysqlconnector://root:1488@localhost:3306/test')

ex = e.execute

# print(ex('ALTER TABLE product ADD COLUMN Date2 datetime default CURRENT_TIMESTAMP'))
# print(ex('CREATE INDEX product_index ON product(Name)'))

# print(ex('ALTER TABLE product ADD CONSTRAINT pk_main PRIMARY KEY(id)'))

print(ex('SELECT Name from product USE INDEX (pk_main)').fetchall())




# ex('CREATE TABLE Parent(id int PRIMARY KEY UNIQUE NOT NULL AUTO_INCREMENT,'
#    '            name varchar(40) NOT NULL)')
#
#
# ex('CREATE TABLE Child(id int PRIMARY KEY UNIQUE NOT NULL AUTO_INCREMENT,'
#    '            name varchar(40) NOT NULL,'
#    '            parent_id int REFERENCES Parent (id) ON DELETE CASCADE)')

# ex('DELETE FROM Child')
# print(ex('ALTER TABLE Child ADD CONSTRAINT FOREIGN KEY(parent_id) REFERENCES Parent (id) ON DELETE CASCADE'))

# print(ex('SELECT * FROM Parent').fetchall())
# print(ex('SELECT * FROM Child').fetchall())
#
# ex("INSERT INTO Parent(name) VALUES ('Top')")
# ex('INSERT INTO Child(id, name, parent_id) VALUES (1,2,2)')
#
# print(ex('SELECT * FROM Parent').fetchall())
# print(ex('SELECT * FROM Child').fetchall())
#
# ex('DELETE FROM Parent')
#
#
# print(ex('SELECT * FROM Parent').fetchall())
# print(ex('SELECT * FROM Child').fetchall())



# print(ex('SELECT DISTINCT * FROM product ORDER BY(Name)').fetchall())
#
# print(ex('SELECT DISTINCT Count FROM product').fetchall())

# print(ex("UPDATE product p SET Name=p.id WHERE p.Name='test'"))

# print(ex("SELECT CONCAT(Name, ' 22') FROM product").fetchall())
#
# print(ex("SELECT * FROM product WHERE Count IS NULL").fetchall())
#
# print(ex("SELECT Name FROM product WHERE NOT(id > 2)").fetchall())
#
# print(ex("SELECT Name FROM product WHERE id BETWEEN 1 AND 3").fetchall())

# print(ex("SELECT Name FROM product WHERE id IN(2,3)").fetchall())

# print(ex("SELECT Name FROM product WHERE Name LIKE 'T%rt_'").fetchall())

# print(ex("SELECT Name FROM product WHERE Name LIKE 'T%rt_' ESCAPE '_'").fetchall())

# print(ex('SELECT CONVERT(id, SIGNED) FROM product').fetchall())

print(ex('SELECT 1 + "1"').fetchall())