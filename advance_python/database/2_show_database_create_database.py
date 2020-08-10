# operations
# create database
# show database

# cursor() method-- this method is used to create cursor class object.
# we need cursor object so we can call execute() methdo
# syntax--> cursor_object.cursor()

# arguments me be passed to the cursor() method to control what type of cursor to create
# if buffered is True, the cursor fetches all rows from the server after an operation is executed. this is useful when quieries return all results set.buffered can be used alone r in combination with the dictionary or named_tuple arguments.

# if dictionary is True, the cursor returns rows as dictionaries

# if named_tuple is True, the cursor returns rows and named tuple

# if prepared is True, the cursor is used for executing preapared statements
# if prepared is True, the cursor is used for executing preapared statements

# if raw is True the cursor skips the conversion from SQL data types to python when fetching rows. a raw cursor is usually used to get bettrer performence or whem you want to do the conversion yourself

# The cursor_clas arguments can be used to pass a class to use for instantiating a new cursor. it must be a subclass of cursor.CursorBase

# the returned object depends on the combination of the arguments

#
# if not buffered and not raw: MYSQLCursor

# if buffered and not raw: MYSQLCursorBuffered

# if not buffered and  raw: MYSQLCursorRaw

# if buffered and  raw: MYSQLCursorBufferedRaw


# execute() method
# this method is used to execute given SQL queries
# we need cursor object so we can call execute() method
# syntax--> cursor_object.execute(sql,param=None,multi=False)
# sql--> it is a sql query
# param--> the parameter found in the tuple or dictionary params are bound to the variables in the operarions
# multi()--> execute() returns an iterator if multi is True

# ex-->
# myc=conn.cursor()
# myc.execute('SELECT * FROM TABLE_NAME')

# or
# query_variable='SELECT * FROM TABLE_NAME'  --> storing the query in a varible and passing the variable in execute method as its parameter
# myc=conn.cursor()
# myc.execute(query_variable)

# close() method
#  this method closes the cursor, resets all results, and ensure that the cursor object has no reference to its original connection object

# syntax--> cursor_object.close()
# myc.close()


# connecting to the database and creating a database and printing all the databases list before and after creating a new database


import mysql.connector

try:
    conn = mysql.connector.connect(user='root', password='Mysql@123')
    if(conn.is_connected()):
        print("Connected sucessfully\n")

except:
    print('connection failed\n')

# printing all the databases
print("Printing all database\n")
sq = 'SHOW DATABASES'
cr = conn.cursor()
cr.execute(sq)  # passing the query
for data in cr:
    # print(data)  # it will return all the database in tuple
    print(list(data))  # converting the database name into list form

cr.close()  # closing the cursor object
# creating a new database
sq1 = 'CREATE DATABASE keshav'
cr1 = conn.cursor()
cr1.execute(sq1)
print("A new databse created sucessfully")

cr1.close()  # closing the cursor object
print("\nthe updated databse list\n")
sq2 = 'SHOW DATABASES'
cr2 = conn.cursor()
cr2.execute(sq2)
for data in cr2:
    print(list(data))

print('done')
cr2.close()  # closing the cursor object
conn.close()  # closing the connection
