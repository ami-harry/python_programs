# make connection with mysql and show databases and add a database and print the updated database

import mysql.connector

try:
    conn = mysql.connector.connect(user='root', password='Mysql@123')
    if(conn.is_connected()):
        print("Connected sucessfully")

except:
    print("Connection failed")

# printing the databsase
qry = 'SHOW DATABASES'
cv = conn.cursor()
cv.execute(qry)
print("The currently databases are: ")
for i in cv:
    print(list(i))

print()

qry1 = 'CREATE DATABASE lenovo'
cv1 = conn.cursor()
cv1.execute(qry1)
print("A new databases has bee created")
print()

# printing the databsase
qry2 = 'SHOW DATABASES'
cv2 = conn.cursor()
cv2.execute(qry2)
print("The updated list of databases are: ")
for i in cv2:
    print(list(i))

cv.close()
cv1.close()
cv2.close()
conn.close()
