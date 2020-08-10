# connecting with database
# connect()--> this method is used to open or establish a new connection. it returns an object representing the connetion.
# syntax--> connection_object=connect(user='root',password='23@dd',database='dbname', host='loalhost',port=3306)


# creating the connection

import mysql.connector
'''
try:
    conn = mysql.connector.connect(
        user='root',
        password='Mysql@123',
        database='Harry',
        host='localhost',
        port=3306)
'''
# or
con_details = {
    'user': 'root',
    'password': 'Mysql@123',
    # 'host': 'localhost',
    'database': 'Harry',
    # 'port': 3306
}

try:
    conn = mysql.connector.connect(**con_details)
    if(conn.is_connected()):
        print("Connecction sucessfull")
except:
    print("Connection failed")

conn.close()
