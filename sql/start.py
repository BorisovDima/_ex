from sqlalchemy import create_engine


engine = create_engine('mysql+mysqlconnector://root:1488@localhost:3306/test')

# engine.execute('DROP TABLE Category')

# engine.execute('CREATE TABLE product ('
#                'id int PRIMARY KEY AUTO_INCREMENT ,'
#                'Name varchar(40) NOT NULL,'
#                'Price int )')
#
#
# engine.execute("Insert into product(Name, Price) values ('T-Shirt', 21)")
#
# engine.execute("ALTER TABLE product MODIFY Price float NOT NULL")
# engine.execute("ALTER TABLE product ADD COLUMN Count int")
# engine.execute("ALTER TABLE product ADD COLUMN Category varchar(30)")
# engine.execute("ALTER TABLE product ADD Sales int")
#
# print(engine.execute("select Name from product").fetchall())
# print(engine.execute("show columns from product").fetchall())

# engine.execute('CREATE TABLE Category ('
#                 'Name varchar(40) NOT NULL )')
#
# engine.execute("Insert into product(Name, Price, Category) values ('T-Shirt1', 21, 'Super')")
# engine.execute("Insert into product(Name, Price, Category) values ('T-Shirt2', 22, 'Mega')")
# engine.execute("Insert into product(Name, Price, Category) values ('T-Shirt3', 23, 'Pika')")
# engine.execute("INSERT INTO Category(Name)"
#                "SELECT DISTINCT Category FROM product "
#                "WHERE Category IS NOT NULL") # DISTINCT = UNIQUE
#
#
# engine.execute("INSERT INTO Category(Name) VALUES ('Bunker')")
# print(engine.execute("select * from Category").fetchall())
# engine.execute("ALTER TABLE Category ADD id int NOT NULL AUTO_INCREMENT PRIMARY KEY")
# print(engine.execute("select * from Category").fetchall())
#
# engine.execute('ALTER TABLE product DROP COLUMN Category')
# engine.execute('ALTER TABLE product ADD COLUMN CategofryID int')

# engine.execute('ALTER TABLE product ADD CONSTRAINT FOREIGN KEY(CategoryID) REFERENCES Category(id)')
# engine.execute('UPDATE product SET CategoryID=(SELECT id FROM Category WHERE id=product.id)')

# engine.execute("INSERT INTO product(Name, CategoryID, price) VALUES ('test', 5, 20)")

# print(engine.execute('SELECT Name, CONCAT(Price, Name) AS p  FROM product').fetchall())
#
# print(engine.execute('SELECT p.Name, p.Price FROM product p').fetchall())
#
# print(engine.execute('SELECT p.Name, p.Price FROM product p WHERE p.Price > 21').fetchall())



# print(engine.execute('SELECT p.Name, c.Name FROM product p '
#                      'INNER JOIN Category c ON p.CategoryID = c.id').fetchall())
#
# engine.execute("INSERT INTO product(Name, price) VALUES ('test', 20)")
#
# print(engine.execute('SELECT p.Name, c.Name FROM product p '
#                      'LEFT JOIN Category c ON p.CategoryID = c.id').fetchall())
#
#
# print(engine.execute('SELECT p.Name, c.Name FROM product p '
#                      'RIGHT JOIN Category c ON p.CategoryID = c.id').fetchall())

e = engine.execute
# e('ALTER TABLE product ADD material int')
# e('ALTER TABLE product ADD CONSTRAINT FOREIGN KEY(material) REFERENCES product(id)')

e('UPDATE product SET material=(SELECT id FROM (SELECT * FROM product WHERE id > 3) AS a LIMIT 1) WHERE id=1')

print(e('SELECT * FROM product').fetchall())