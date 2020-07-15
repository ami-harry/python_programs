# insert method
# this is used to insert new the element at specific position no.

# syntax--> list_name.insert(position_no,new_element)

# taking input to list
# printing and asking where he want to add element
# again print the list

a = []  # empty list
size_of_list = int(input("Enter the size of the list:"))

for data in range(size_of_list):
    print("Enter element for index no ", data, end='')
    a.append(input(": "))

print("Original list", a)

# taking input at which position he want to change the element
pos = int(input("Enter the position where you want to add the new element"))
ele = input("Enter the new element for that position")

a.insert(pos, ele)
print()
print("The updated array is :", a)
