import mysql.connector
mydb=mysql.connector.connect(host='localhost',user='root',password='Deeksha@1010')
print(mydb.connection_id)

