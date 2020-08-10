import mysql.connector
# database
# database is integrated collection of related information along with the details so that ut us available to the several user for the different application

# python supports various databases
# MYSQL
# MS-SQL
# SQLite
# MongoDB
# Oracke OC18
# Postgre SQL
# firebirds
# Ms Access


# MYSQL
# MYSQL is an open source database management systen application which will help us to manage the database like store and retrieve data.

# main operations with databsse
# CRUD(c-->create, r-->read,  u-->update,  d-->delete)


# requirements
# SQL--> to write sql queries
# MYSQL--> we have to install MYSQL in our system.
# connector or driver--> a connector is a progrm that establishes connection between python programs and MYSQL database, without installing connetor it is not possible to make communication between python program and SQL database

# to work with MYSQL in python program we have to import connector sub module of MYSQL module.
# import mysql.connector


# port and localhost is bydefault, it is same always, we can avoid to writing it everytime


# creating connection

# connect()--> this method is used to open or establish a new connection. it returns an object representing the connection
# syntax--> conection_object=mysql.connector.connect(user='root',password='abc@123', host='localhost' port=3306)


# creating connection(another method using dictionary--> key:value pair)
'''
import mysql.connector


config = {
    'user': 'root',
    'password': 'Mysql@123',
    'host': 'localhost',
    'port': 3306
}
# creating the connection using values in this dict

conn = mysql.connector.connect(**config)

'''

'''

# using try-except to catch the error

import mysql.connector

try:
    conn = mysql.connector.connect(host='localhost',
                                   database='Harry',
                                   user='root',
                                   password='Mysql@123')
    print("Connected")
except:
    print("Connection failed")

'''


#  check connection
# is_connected()--> this method is used to check if the connection  to mysql is established or not. it returns True if the connetion is established sucessfully.
# syntax--> connection_object.is_connected()

'''

try:
    conn = mysql.connector.connect(user='root', password='Mysql@123')
    if(conn.is_connected()):  # checking the condition
        print("Connection established")

except:
    print("Connection failed")

'''


# closing the connection
# close() --> this method is used to close/disconnect the connection
# syntax--> connector_obj.close()

# after close statement we cant perform any action with that database


details = {
    'user': 'root', 'password': 'Mysql@123'
}

try:
    conn = mysql.connector.connect(**details)
    if(conn.is_connected()):
        print("Cnnection sucessful")


except:
    print("Connetion failed\n")

print("before close", conn.is_connected())
conn.close()  # closing the connection
print("after close", conn.is_connected())
