# create a database and make tables inside it and show it before and after creating the table

'''
import mysql.connector
try:
    conn = mysql.connector.connect(user='root', password='Mysql@123')
    if(conn.is_connected()):
        print("Connected ")
except:
    print("Connection failed")


# showing the previous databases list
print("The present databases are:")
q = 'SHOW DATABASES'
ob = conn.cursor()
ob.execute(q)
for d in ob:
    print(list(d))


# creating the databse
q1 = 'CREATE DATABASE student_details'
ob1 = conn.cursor()
ob1.execute(q1)

# printing the updated databases list
q3 = 'SHOW DATABASES'
ob2 = conn.cursor()
ob2.execute(q3)
for d in ob2:
    print(list(d))

ob.close()
ob1.close()
ob2.close()
conn.close()
'''


# showing the tables of databse student_details
import mysql.connector
try:
    conn = mysql.connector.connect(
        user='root',
        password='Mysql@123',
        database='student_details')
    if(conn.is_connected()):
        print("Connected")
except:
    print("connection failed sucessfully")

# showing the tables before creating
q1 = 'SHOW TABLES'
c1 = conn.cursor()
c1.execute(q1)
for t in c1:
    print(t)
print()
# creating the table

q2 = 'CREATE TABLE student(stu_ID INT AUTO_INCREMENT PRIMARY KEY,stu_NAME VARCHAR(20), sty_ROLL INT, stu_FEES FLOAT)'
c2 = conn.cursor()
c2.execute(q2)
print(" 1 Table created ")
print()

# printing the tables
q3 = 'SHOW TABLES'
c3 = conn.cursor()
c3.execute(q3)
for t in c3:
    print(t)
print("done")

c1.close()
c2.close()
c3.close()
conn.close()
