# extend method
# this method is used to append anoter list or iterable object at the end of the list
# syntax--> list_name.extend(lst)

# this method simply add two lists in one list from the end of first list
# it returns nothing..we cant store the returned list into a new list.
first_list = []  # empty list
size = int(input("Enter the size of the first list : "))
# taking input
data = 0
for data in range(size):
    print("Enter the element for index no", data, end='')
    first_list.append(input(": "))

second_list = []  # empty list
size = int(input("Enter the size of the second list : "))
# taking input
data = 0
for data in range(size):
    print("Enter the element for index no", data, end='')
    second_list.append(input(": "))

print("The original first list is ", first_list)
print("The original second list is ", second_list)
print()
print("Extending list2 in list1 , and the updated list is:")
print()

first_list.extend(second_list)
print("The updated list is ", first_list)