# writing data into a file as per user input and then reading the stored data
# write data into a file as per user input

size = int(input("Enter the size of list:"))

lst1 = []
for data in range(1, size+1):
    print("Enter ", data, "st student name: ", end='')
    lst1.append(input(": "))

lst2 = []
for data in range(1, size+1):
    print("Enter ", data, "nd student roll: ", end='')
    lst2.append(input(": "))

lst3 = []
for data in range(1, size+1):
    print("Enter ", data, "rd student year: ", end='')
    lst3.append(input(": "))

# writing the data
with open('user_inp.txt', mode='x') as data:
    data.write("Name:")
    data.write(str(lst1))
    data.write("\nRoll:")
    data.write(str(lst2))
    data.write("\nYear:")
    data.write(str(lst3))
print("data wtitten sucess")


# reading the data
with open('user_inp.txt') as data:
    file_data = data.read()
    print(file_data)
