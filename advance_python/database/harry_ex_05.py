# make a new database and create its table
import mysql.connector

try:
    conn = mysql.connector.connect(user='root',
                                   password='Mysql@123')
    if(conn.is_connected()):
        print("Connrected")
except:
    print("not connected")

# prinnting the databases
q1 = 'SHOW DATABASES'
cl_obj1 = conn.cursor()
cl_obj1.execute(q1)
for d in cl_obj1:
    print(list(d))
print()

# creating a new database
db_name = input("Enter the name for your database: ")
q2 = f'CREATE DATABASE {db_name}'
cl_obj2 = conn.cursor()
cl_obj2.execute(q2)
print(f"One new database {db_name} created ")

print()
print("the updated database list is:")
cl_obj3 = conn.cursor()
cl_obj3.execute(q1)
for d in cl_obj3:
    print(list(d))
print()

# take input which database he wants to you and want to make tables inside it
db_use = input("Enter which database you want to use: ")
q3 = F'USE {db_use}'
cl_obj4 = conn.cursor()
cl_obj4.execute(q3)
print(f"Database change to {db_use}  ")

# creating table
t_name = input("Enter name for the table: ")
t_c_h1 = input("Enter first col first heading: ")
t_c_h2 = input("Enter first col second heading: ")
t_c_h3 = input("Enter first col third heading: ")
t_c_h4 = input("Enter first col forth heading: ")


q4 = f'CREATE TABLE {t_name}({t_c_h1} INT AUTO_INCREMENT PRIMARY KEY,{t_c_h2} VARCHAR(20),{t_c_h3} INT,{t_c_h4} FLOAT)'
cl_obj5 = conn.cursor()
cl_obj5.execute(q4)
print(f"table {t_name} created in database {db_use}")
print()

# deleting the database
db_drop = input("Enter db name to delete: ")
q5 = f'DROP DATABASE {db_drop}'
cl_obj6 = conn.cursor()
cl_obj6.execute(q5)
print(f"one database {db_drop} delete: ")

# after deletion the updated database is
print("the updated database list is")
cl_obj7 = conn.cursor()
cl_obj7.execute(q1)
for d in cl_obj7:
    print(list(d))
print('\ndone')


cl_obj1.close()
cl_obj2.close()
cl_obj3.close()
cl_obj4.close()
cl_obj5.close()
cl_obj6.close()
cl_obj7.close()
conn.close()
