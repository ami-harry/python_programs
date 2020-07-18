# list of tuples

# here in the list , the elements can be in many forms
# the elements can be integer, string, tuple, dictionary, set and all
# to access these kind of list having various type of elements we have to check the condition for every element that it is a tuple ot not

# in the other hand, if the list has elemens only in the form of  tuple.. to access this list of tuple is not difficult, we dont need to check the condition
# we can easily access its elements becuase here all the elements are of tuple


'''



a = [35, 'harry', 'hk', ('this is tuple', 'in the list',
                         'as an element'), 45, 23, 56, 'this is element of tuple as string']

# this list has various type of elements so we need to check the conditions for every element

# accessing elements of this tuples using for loop with index
print("the original list is")
print(a)
print()


#  accessing using for loop
print("Printing the data with index using for loop")
for i in range(len(a)):
    if type(a[i]) is tuple:
        if len(a[i]) > 1:
            for j in range(len(a[i])):
                print("at position no ", i, " of its index ",
                      j, " the value is ", a[i][j])
    else:
        print("at position ", i, " the element is ", a[i])

print()


# without index
print("Printing the data without index using for loop")
for i in range(len(a)):
    if type(a[i]) is tuple:
        if len(a[i]) > 1:
            for j in range(len(a[i])):
                print(a[i][j])
    else:
        print(a[i])

print('done')

print()
# accessing using while loop
print("Printing the data with index using while loop")
i = 0
while i in range(len(a)):
    if type(a[i]) is tuple:
        if len(a[i]) > 1:
            j = 0
            while j in range(len(a[i])):
                print("at position no ", i, " of its index ",
                      j, " the value is ", a[i][j])
                j += 1
            i += 1
    else:
        print("at position ", i, " the value is ", a[i])
        i += 1
print('done')
print()
print("Printing the data without index using while loop")
i = 0
while i in range(len(a)):
    if type(a[i]) is tuple:
        if len(a[i]) > 1:
            j = 0
            while j in range(len(a[i])):
                print(a[i][j])
                j += 1
            i += 1
    else:
        print(a[i])
        i += 1
print('done')



'''


# accessing the list having elements only as tuples
# all the elements are of same type
# all are tuples and there are as individual element of list

a = [(34, 23, 5, 'hii'), ('hello', 34, 23, 54),
     ('hmm', 'achha', 343, 543), ('thik hai', 46, 23, 'bye')]

# here in this list the elements are as tuple.
#  so we dont need to check the condition
# we can easily access this

print("the original list is ")
print(a)
print()
# accessing the elements of this list using for loop
print("Accessing elements using for loop without index:")
for i in a:
    for j in i:
        print(j)
print('done')
print()
print("Accessing elements using for loop with index:")

for i in range(len(a)):
    for j in range(len(a[i])):
        print("at row ", i, " and  col ",
              j, " the value is ", a[i][j])
print('done')
print()

# accssing using while loop
print("Accessing elements using while loop with index:")
i = 0
while i in range(len(a)):
    j = 0
    while j in range(len(a[i])):
        print("at row ", i, " and  col ", j, " the value is ", a[i][j])
        j += 1
    i += 1
print('done')
print()
print("Accessing elements using while loop without index:")
i = 0
while i in range(len(a)):
    j = 0
    while j in range(len(a[i])):
        print(a[i][j])
        j += 1
    i += 1
print('done')
print()
