# make a tuple
# take input
# access the elements using for loop with index and without index
# with for loop and while loop


# we will make a empty list a will take input and will typecase it into tuple then we will access that tuple using loops


lst1 = []  # this is empty list
size = int(input("Enter the size for first tuple: "))

# taking input
for data in range(size):
    print("Enter the element for index no ", data, end='')
    lst1.append(input(": "))

# print("the data is ", lst1)
# print("Its type is ", type(lst1))
# print("here it is list type, we will type case it into tuple: ")
lst1 = tuple(lst1)
# print("Now its type is ", type(lst1))
# print("The data of lst1 is ", lst1)
print()
lst2 = []  # this is empty list
size = int(input("Enter the size for the second tuple: "))

# taking input
for data in range(size):
    print("Enter the element for index no ", data, end='')
    lst2.append(input(": "))

# print("the data is ", lst2)
# print("Its type is ", type(lst2))
# print("here it is list type, we will type case it into tuple: ")
lst2 = tuple(lst2)
# print("Now its type is ", type(lst2))
# print("The data of lst2 is ", lst2)

print()


# making a new tuple having those two tuples which user has given as input
'''
a = lst1+lst2 # making a new tuple with concatination
# now accessing the elements for the tuple using for loop

for i in range(len(a)):
    if type(a[i]) is tuple:
        if len(a[i]) > 1:
            for j in range(len(a[i])):
                print("at index no ", i, " of its index no ",
                      j, " the value is ", a[i][j])
    else:
        print("at index ", i, " the value is ", a[i])

print("out of loop")

# without index

for i in a:
    for j in i:
        print(j)
    print()

print("out of loop")
'''


# a = ((lst1), (lst2)) here we are making a tuple which having 2 tuples as its element
a1 = ((lst1), (lst2))
# this is a tuple having its element is also a tuple
print("the data of lst1 is ", lst1)
print()
print("the data of lst2 is ", lst2)
print()
print("the data of both tuples are a1", a1)
print()

# accessing the elements of this tuple using for loop with index
# to accesss this tuple we need not to check the condtion for every element  that its type is tuple or not
# becuase its elements are alredy a tuple

print("printing the element with index:")
for i in range(len(a1)):
    for j in range(len(a1[i])):
        print("At index ", i, " of its index ", j, " the value is", a1[i][j])

print('done')


print()
# without index
print("printing the data using for loop without index")
for i in a1:
    for j in i:
        print(j)

print('done')
