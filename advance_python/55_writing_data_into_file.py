# writing data into file
# write()--> This method is used to write/store character or group of string into the file represented by the file object. it returns the numbre of character written

# syntax--> file_object.write(string)

'''

f = open('hk.txt', mode='a')
nc = f.write("This line is appending to the file ")
print("No of character added is ", nc)
f.close()
print("data in the file added sucessfully")

'''

# writelines()--> this method is used to store/write group of string(list/tuple/set) into the file represented by the file object
# syntax--> file_object.writeline(group of string)

f = open('hariom.txt', mode='a')
lst = ['Harry ', 'Hariom ', 'Shalini ', 'Keshav ']
f.writelines(lst)
f.close()
print("Data added sucessfully")
