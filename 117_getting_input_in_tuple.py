# geeting input from user in tuple
# as tuple is immutable object we cant take input in it directly
# we have various methods to take input in tuple
#  we will take input in list after that we will convert that list into tuple
# memory issue can be there in this method for huge amount of data


a = []  # empty list
size = int(input("Enter the size of the list: "))

# taking elements input
for ele in range(size):
    print("Enter element for index no ", ele, end='')
    a.append(input(": "))

# printing the original list
print()
print("Your input list was: ", a)
print()
print(type(a))
print("here it is list now, we are changing its type into tuple")
# changing the type from list into tuple
a = tuple(a)
# printing the changed type
print(type(a))

print()
print("Printing the tuple elements ")
print(a)
print()
print("tuple elemenets using for loop with index")
for ele in range(len(a)):
    print("at index no", ele, " the element is ", a[ele])

print()
print("the elements of tuple without index using while loop is :")
ele = 0
while ele in range(len(a)):
    print(a[ele])
    ele += 1


print()
print("done")
print()
