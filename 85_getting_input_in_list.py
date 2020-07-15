# getting input in list
# a. first we will make a empty list
# b. then we will ask the user for the size of the list
# using loop we will take input using append method
# yes but keep in mind which type of data  have to take input


a = []  # empty list
size_of_list = int(input("Enter the size of the list: "))
print("Enter ",size_of_list," for the list")

# taking input using loop
# data = 0
# for data in range(size_of_list):
# print("Enter the data for index no ", data, end='')
# a.append(input(": "))
# print()

data = 0
while data in range(size_of_list):
    print("Enter the data for index no ", data, end='')
    a.append(input(": "))
    data += 1

print()
print("Printing the list as your input")
data = 0
while data in range(len(a)):
    print("At index no ", data, " the value is ", a[data])
    data += 1
print("Done")
