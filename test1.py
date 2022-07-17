import mysql.connector as connection

mydb = connection.connect(host = "localhost",
                          user = "root",
                          passwd = "Reset@123")
cursor = mydb.cursor()
s = "create table abhinay.details(name varchar(20), age int(2))"
cursor.execute(s)