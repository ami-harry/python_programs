# list concatination
# list concatination can be done using + operator between the two lists

first_list = []  # empty list
size = int(input("Enter the size of the list : "))
# taking input
data = 0
for data in range(size):
    print("Enter the element for index no", data, end='')
    first_list.append(input(": "))
print("The original list is ", first_list)


second_list = []  # empty list
size = int(input("Enter the size of the list : "))
# taking input
data = 0
for data in range(size):
    print("Enter the element for index no", data, end='')
    second_list.append(input(": "))
print("The original list is ", second_list)

con_list = first_list+second_list
# storinf the elemets of first list and second list in the concatinated list
print("The list after concatination is:\n", con_list)

# the major difference between concatination and extend method is that
# concatination add the list and it is sotred in a new list and in extend method the elements of adding list is added after the last element of the first list and it returns nothing
# in extend method a list is added at the end of a existing list but in contaction lists are added in a new variable
