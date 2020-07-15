# clear method
# this method is used to delete the all elements of the list
#
# syntax >--> list_name.clear()


a = []  # empty list
size = int(input("Enter the size of the list : "))
# taking input
data = 0
for data in range(size):
    print("Enter the element for index no", data, end='')
    a.append(input(": "))
print("The original list is ", a)


# it will delete all the elements of the existing list and ,
# this will return nothig so dont try to store it in a variable. it will return none
# b = a.clear()
# print("The list after clear method call :", b)
# like this
