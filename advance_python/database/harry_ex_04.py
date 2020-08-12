# make connection with mysql
# show database list
# create a database as per user input
# change the databse as per user input
# and show tables of database as per user input
# deteling the database and making the new database


import mysql.connector

try:
    conn = mysql.connector.connect(user='root',
                                   password='Mysql@123'
                                   )
    if(conn.is_connected()):
        print("Connected sucessfully")
except:
    print("Connection failed")

print("printing the database list: ")
q1 = 'SHOW DATABASES'
crscr_obj1 = conn.cursor()
crscr_obj1.execute(q1)
for d1 in crscr_obj1:
    print(list(d1))
print()
'''
# asking the user to enter database name to create the new database
cr_db = input("Enter the name for databse: ")
q2 = f'CREATE DATABASE {cr_db}'
crscr_obj2 = conn.cursor()
crscr_obj2.execute(q2)
print(f"new database {cr_db} is created ")
print()

# printing the updated list of databse

print("printing the database list after creating a new one: ")
q3 = 'SHOW DATABASES'
crscr_obj3 = conn.cursor()
crscr_obj3.execute(q3)
for d1 in crscr_obj3:
    print(list(d1))


print()
# asking the user for database name to change the database
ch_db = input("Enter database name to change into: ")
q4 = f'USE {ch_db}'
crscr_obj4 = conn.cursor()
crscr_obj4.execute(q4)
print(f"Database changed to {ch_db}")
print()

# asking the user to enter database name to show the tables of it

q5 = 'SHOW TABLES'
crscr_obj5 = conn.cursor()
crscr_obj5.execute(q5)
print(f"Printing the tables of {ch_db} database:")
for t in crscr_obj5:
    print(list(t))
print()

'''

# deleting the databse
del_db = input("Enter the database name to delete :")
q6 = f'DROP DATABASE {del_db}'
crscr_obj6 = conn.cursor()
crscr_obj6.execute(q6)
print(f'one database deleted {del_db}')
print()
print('printing the updated databse list:')

crscr_obj7 = conn.cursor()
crscr_obj7.execute(q1)
print("The updated database list is:")
for db in crscr_obj7:
    print(list(db))
print()


crscr_obj1.close()
# crscr_obj2.close()
# crscr_obj3.close()
# crscr_obj4.close()
# crscr_obj5.close()
crscr_obj6.close()
crscr_obj7.close()
conn.close()
