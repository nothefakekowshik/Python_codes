import mysql.connector
mydb=mysql.connector.connect(
    
    host="localhost",
    user="root",
    passwd="kowshiknarasimha@1",
    database="testing"

)
mycursor=mydb.cursor()
#mycursor.execute("create table students(name varchar(20),roll_n int(10))")
#mycursor.execute("insert into students values('kowshik',60)")
name=input("enter the name")
roll=int(input("Enter your number"))
sql = "INSERT INTO students (name, roll_n) VALUES (%s, %s)"
val = (name,roll)
mycursor.execute(sql, val)
# mycursor.execute("insert into students values(name,roll)")
	