# copy list
# copy() method is used to copy all the elements of a list to another list
# when we have a list of seperatred copy of all elements is stored in another list. both are independent
# both have their own address
# modification will effect in the same list
'''

my_list = []  # empty list
size = int(input("Enter the size of the list : "))
# taking input
data = 0
for data in range(size):
    print("Enter the element for index no", data, end='')
    my_list.append(input(": "))
print("The original list is ", my_list)

# copying the data of my_list into a new list
#  but the copied new list have a seperate memory location
new_list = my_list.copy()

# checking the address of both list
print()
print("Address of the original list is ", id(my_list))
print("Address of the copied list is ", id(new_list))
print()

# modifying the values of both list
my_list[3] = "Harry"
new_list[3] = "ishrat"
print("The list after modification", my_list)
print("The list after modification", new_list)
'''


# cloning list
# we can cloning a list into another list using slicing.
# when we clone a list in a seperate copy of all the elements is stored in another list. both the list are independent.
# it is also a copy of list but the method of copying is different
# here also the new list have a different address

my_list = []  # empty list
size = int(input("Enter the size of the list : "))
# taking input
data = 0
for data in range(size):
    print("Enter the element for index no", data, end='')
    my_list.append(input(": "))
print("The original list is ", my_list)

# slicing my_list into new_list
#  but the cloned new list have a seperate memory location
# here we are slicing all the elements of the list and storing it into  new list ,
new_list = my_list[:]

# checking the address of both list
print()
print("Address of the original list is ", id(my_list))
print("Address of the copied list is ", id(new_list))
print()

# modifying the values of both list
my_list[3] = "Harry"
new_list[3] = "ishrat"
print("The list after modification", my_list)
print("The list after modification", new_list)
