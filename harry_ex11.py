# make an empty set and update its values using list by user input
# make an empty list and ask size, take input and print the data



a = set()  # this is empty set
b = []  # empty list
# taking input in list and putting the list into set
size = int(input("Enter the size of the list : "))

for data in range(size):
    print("Enter the element for index no ", data, end='')
    b.append(input(": "))

print("The list is ")
print(b)
print(type(b))
print(id(b))
print()

# updating the set value with this list value using update method
print("The original set is ")
print(a)
print(type(a))
print(id(a))
print()

a.update(b)

print("The updated set is")
print(a)
print(type(a))
print(id(a))