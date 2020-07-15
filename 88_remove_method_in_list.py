# remove() method
# this method is used to remove the first occerence of given element from the existing list.
# if it doesn't finf the element it shows ValueError.

# syntax--> list_name.remove(element)

a = []  # empty list
size = int(input("Enter the size of the list : "))
# taking input
data = 0
for data in range(size):
    print("Enter the element for index no", data, end='')
    a.append(input(": "))
print("The original list is ", a)

rem_ele = input("Enter the element you want to delete: ")
a.remove(rem_ele)
print()
print("List after remove element", a)

# remove function remove a element..if the element exists more than one time it will delete it form the starting which comes first