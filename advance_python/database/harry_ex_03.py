# make connetion with mysql and show databases


import mysql.connector

data1 = {
    'user': 'root',
    'password': 'Mysql@123'
}
try:
    conn1 = mysql.connector.connect(**data1)
    if(conn1.is_connected()):
        print("Connected sucessfully!")
except:
    print("Connection faild sucessfully")

# showing the databases
q1 = 'SHOW DATABASES'
cr_obj1 = conn1.cursor()
cr_obj1.execute(q1)
# printing the databases list
for data in cr_obj1:
    print(list(data))
print()


name = input("Enter the database name: ")
q2 = f'USE {name}'
cr_obj2 = conn1.cursor()
cr_obj2.execute(q2)
print(f"database changed to {name}")
print()


print(f'printing the tables of {name} database')
q3 = 'SHOW TABLES'
cr_obj3 = conn1.cursor()
cr_obj3.execute(q3)
for t in cr_obj3:
    print(list(t))


cr_obj1.close()
cr_obj2.close()
cr_obj3.close()


conn1.close()
