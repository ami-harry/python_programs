# sort()
# this method is used to sort the elements of the list in ascending order .
# syntax --> list_name.sort()
a = []  # empty list
size = int(input("Enter the size of the list : "))
# taking input
data = 0
for data in range(size):
    print("Enter the element for index no", data, end='')
    a.append(input(": "))
print("The original list is ", a)

a.sort()
print("The list after sorting: ", a)

# if the list has interger, float and string both
# sort method firstly sorts the int and float  value together, then string by alphabetic order
