# accessing the nested loop using while loop


'''
a = (10, 20, 30, ('harry', 'hk'))
# accesing this nested tuple with index using for loop
# this tuple has elements as integer  and a list also
#  so for accessing it we have to check a condition that the accessing element is a list or not
# after that we can access that list as element


print("The original tuple is ", a)
print()
# accessing the element using index
print('accessing the element using index ')
i = 0
while i in range(len(a)):
    if type(a[i]) is tuple:
        if len(a[i]) > 1:
            j = 0
            while j in range(len(a[i])):
                print("at index ", i, " of its index ",
                      j, " the value is ", a[i][j])
                j += 1
            i += 1
    else:
        print("at index ", i, " the value is ", a[i])
        i += 1
print("out of loop")


# without index
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
print("out of loop")
'''

a = ((10, 20, 30), (34, 45, 54))
# for accessing this tuple we need not to check the condition that the elemets are tuple or not becuase all the elements of this tuple is already a tuple. so we can essily access it


# accessing this using while loop with index
i = 0
while i in range(len(a)):
    j = 0
    while j in range(len(a[i])):
        print("At index ", i, " of its index ", j, " the value is ", a[i][j])
        j += 1
    i += 1
print("out of loop")
print()


# accessing this using while loop without index
i = 0
while i in range(len(a)):
    j = 0
    while j in range(len(a[i])):
        print(a[i][j])
        j += 1
    i += 1
print("Out of loop")
