import mysql.connector
mydb=mysql.connector.connect(host='localhost',user='root',password='Deeksha@1010',database = 'Inventory_Management')
cur=mydb.cursor()

#Creating tables
m='CREATE TABLE manufacture (manufacture_id INT PRIMARY KEY,product_name VARCHAR(30),color VARCHAR(30),quantity INT NOT NULL,Defective_Items INT,Manufacture_Date DATE NOT NULL)'
cur.execute(m)

g='CREATE TABLE goods (goods_id INT PRIMARY KEY ,product_name VARCHAR(30) NOT NULL,color VARCHAR(30) NOT NULL,quantity INT NOT NULL,manufacture_date DATE NOT NULL)'
cur.execute(g)

p='CREATE TABLE purchase (purchase_id INT PRIMARY KEY,store_name VARCHAR(30) NOT NULL, product_name VARCHAR(30) NOT NULL,color VARCHAR(50) NOT NULL, quantity INT NOT NULL, purchase_date DATE NOT NULL)'
cur.execute(p)

s='CREATE TABLE sale (sale_id INT PRIMARY KEY, store_name VARCHAR(30) NOT NULL,product_name VARCHAR(30) NOT NULL, color VARCHAR(30) NOT NULL,quantity INT NOT NULL,sale_date DATE NOT NULL, sale_price float NOT NULL,cost_price float NOT NULL,profit_margin float NOT NULL,Company varchar(30))'
cur.execute(s)

#inserting values
z='INSERT INTO manufacture (manufacture_id,product_name, color, quantity, manufacture_date)VALUES(%s,%s,%s,%s,%s)'
a=[(501,'Wooden Chair', 'Brown', 100, '2023-01-15'),(502,'Wooden table', 'White', 50, '2023-02-02'),(503,'Red Toy Car', 'Red', 200, '2023-02-18'),(504,'Blue Toy Car', 'Blue', 150, '2023-03-03'),(505,'Shirt', 'Blue', 300, '2023-04-01')]
cur.executemany(z,a)
mydb.commit()

x='INSERT INTO goods (goods_id,product_name, color, quantity, manufacture_date)VALUES(%s,%s,%s,%s,%s)'
b=[(101,'Wooden Chair', 'Brown', 80, '2023-01-15'),(102,'Wooden table', 'White', 40, '2023-02-02'),(103,'Red Toy Car', 'Red', 150, '2023-02-18'),(104,'Blue Toy Car', 'Blue', 100, '2023-03-03')]
cur.executemany(x,b)
mydb.commit()

y='INSERT INTO purchase (purchase_id,store_name, product_name, color, quantity, purchase_date)VALUES(%s,%s,%s,%s,%s,%s)'
c=[(201,'MyKids', 'Red Toy Car', 'Red', 50, '2023-02-20'),(202,'MyKids', 'Blue Toy Car', 'Blue', 30, '2023-03-05'),(203,'ORay', 'Shirt', 'Blue', 100, '2023-04-02'),(204,'MyCare', 'Wooden Table', 'Brown', 1, '2023-04-20')]
cur.executemany(y,c)
mydb.commit()

p='INSERT INTO sale(sale_id,store_name, product_name, color, quantity, sale_date, sale_price, cost_price, profit_margin,Company) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
d=[(300,'MYCare', 'wooden table', 'Red', 40, '2023-02-25', 20,10,10,"SS Export"),(301,"ABC","green car","green",50,'2023-02-25',11,10,1,"pqr")]
cur.executemany(p,d)
mydb.commit()

#for question 8
u='UPDATE manufacture SET quantity = quantity - (SELECT SUM(quantity) FROM purchase WHERE color = "Red" AND store_name = "MyKids" )WHERE color = "Red"'
cur.execute(u)

# for question 9
s='SELECT * FROM goods WHERE product_name = "Wooden Chair" AND manufacture_date < "2023-05-01"'
cur.execute(s)
display=cur.fetchall()
for i in display:
    print(i)

#for question 10
profit='select sale_price - cost_price as profit_margin from sale where product_name = "Wooden table" and  store_name = "MYCare" and Company = "SS Export"'
cur.execute(profit)
display2=cur.fetchall()
for t in display2:
   print(t)

#for question 7

d1='DELETE FROM purchase where product_name = "shirt" and  purchase_date ="2023-04-1" and store_name = "ORay"'
cur.execute(d1)
