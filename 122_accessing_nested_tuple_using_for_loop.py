# accessing nested tuples
# this can also be accessed as we access list
'''
a = (10, 20, 30, ('harry', 'hk'))
# accesing this nested tuple with index using for loop
# this tuple has elements as integer  and a list also
#  so for accessing it we have to check a condition that the accessing element is a list or not
# after that we can access that list as element

for i in range(len(a)):
    if type(a[i]) is tuple:
        if len(a[i]) > 1:
            for j in range(len(a[i])):
                print("at index no ", i, " of its index ",
                      j, " the value is ", a[i][j])
    else:
        print("At index ", i, " the value is ", a[i])
print("Done")
print()

# without index
i = 0
j = 0
for i in range(len(a)):
    if type(a[i]) is tuple:
        if len(a[i]) > 1:
            for j in range(len(a[i])):
                print(a[i][j])
    else:
        print(a[i])
print("Done")
'''

# in the above case the tuple elenents were integers and a tuple as an element also
# here we are taking a tuple which has only tuple as element. means here tuples are as an element


a1 = ((10, 'hello', 'hii'), (234, 45, 'hmmm'))
print("The original tuple is ", a1)

# to access this tuple we dont need to check the condition becuase for this tuple the elements are already a tuple so accessing is simple here. no need to check the type for every element

# without index
print()
print("Printing the elements without index:")
for i in a1:
    for j in i:
        print(j)


print()
# with index using for loop
print("Values using index ")
for i in range(len(a1)):
    for j in range(len(a1[i])):
        print("At index ",i," of its index ",j," the element is ",a1[i][j])
print('done')