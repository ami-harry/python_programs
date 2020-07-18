# tuple of list

# tuple of list have also two types of elements
# in first case the tuple has mixture of elements as interger, string and list
# to access this tuple we have to check the condition for every element

# in other hand a tuple has elements only as list
# lists are as an element of the tuple
# to access such tuple of list is easy for us that we dont't need to check the condition for every element


'''

a = (34, 23, 'hii', 'hello', [34, 23, 'this is list'], 23)
# this tuples has mixture of elements as int, string, and a list also
#  to acces its we have to check the condition for every element


# modifying the tuple
# modification is not possible in tuple
# but we can modify the list in inside the tuple
# we will modify the list using index no which is inside the tuple

print("The original tuple is:")
print(a)
print(id(a))
print(type(a))
print()
# modifying the list of tuple
a[4][2] = 'this is modified'
print("After modification the tuple is")
print(a)
print(id(a))
print(type(a))
print()
# accessing the element of this tuple using for loop
print("printing the elements of the list using for loop with index")
for i in range(len(a)):
    if type(a[i]) is list:
        if len(a[i]) > 1:
            for j in range(len(a[i])):
                print(" at pos ", i, " of its ", j, " the value is ", a[i][j])
    else:
        print("at pos ", i, " the value is ", a[i])
print()

print("printing the elements of the list using for loop without index")
for i in range(len(a)):
    if type(a[i]) is list:
        if len(a[i]) > 1:
            for j in range(len(a[i])):
                print(a[i][j])
    else:
        print(a[i])
print()

# accessing the element of this tuple using while loop
print("printing the elements of the list using while loop with index")
i = 0
while i in range(len(a)):
    if type(a[i]) is list:
        if len(a[i]) > 1:
            j = 0
            while j in range(len(a[i])):
                print("at pos ", i, " of its ", j, " the value is ", a[i][j])
                j += 1
            i += 1
    else:
        print("at pos ",i," the value is ",a[i])
        i += 1
print()
print()


'''


a = ([54, 23, 67], ['hii', 'hello', 34], [
     45, 23, 'hmm'], ['achha', 'bholenath', 54])
# in this tuple all the elements are in form of list
# we don't need to check the condition for every element
# we can easily modify this tuple using index of its list

print("The original tuple is ")
print(a)
print(id(a))
print(type(a))

# modifying the element
a[0][1] = 'arijit'
a[3][1] = 234
print("after modification the tuple is")
print(a)
print(id(a))
print(type(a))
print()

# accessing the elements of this tuple using loops
# with index
print('accessing the elements using for loop with index')
for i in range(len(a)):
    for j in range(len(a[i])):
        print("at row ", i, " and col ", j, " the value is ", a[i][j])
print()
# without index
print('accessing the elements using for loop without index')
for i in range(len(a)):
    for j in range(len(a[i])):
        print(a[i][j])
print()

# with index using while loop
print('accessing the elements using while loop with index')
i = 0
while i in range(len(a)):
    j = 0
    while j in range(len(a[i])):
        print("at row ", i, " and col ", j, " the value is ", a[i][j])
        j += 1
    i += 1
print()
# without index
print('accessing the elements using while loop withouy index')
i = 0
while i in range(len(a)):
    j = 0
    while j in range(len(a[i])):
        print(a[i][j])
        j += 1
    i += 1
print()
