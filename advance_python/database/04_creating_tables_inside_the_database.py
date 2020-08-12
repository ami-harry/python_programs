# creating table inside the databse
import mysql.connector

try:
    conn = mysql.connector.connect(
        user='root',
        password='Mysql@123',
        database='Harry')
    if(conn.is_connected()):
        print("Connected sucessfully\n")

except:
    print("Connection failed")

# creating the table inside the database
# viewing the table before creating inside the database Harry

print("Printing the tables inside the databse Harry\n")
qry = 'SHOW TABLES'
crscr_obj = conn.cursor()
crscr_obj.execute(qry)
for t in crscr_obj:
    print(t)

# creating the table inside the database
create_qry = 'CREATE TABLE student(stuID INT AUTO_INCREMENT PRIMARY KEY, stuNAME VARCHAR(25), stuROLL INT, stuFEES FLOAT)'
crscr_object = conn.cursor()
crscr_object.execute(create_qry)
print("Table created sucessfully\n")

# printing the tables after creating
print("Printing the tables inside the databse Harry\n")
qry1 = 'SHOW TABLES'
crscr_obj1 = conn.cursor()
crscr_obj1.execute(qry)
for t in crscr_obj1:
    print(t)


crscr_obj.close()
crscr_object.close()
crscr_obj1.close()
conn.close()
