# accessing the nested list using while loop
'''
# this list is haing elements as interger, float , string and a list also. so to access this the method will be different., we have to check the type of element then after we will print that element
a = [23, 4, "harry", 34.34, ["hariom", 34, 23], 34, 234, ["hello", "hii"]]
print("The original list is ", a)
print("The length of the list is " ,len(a))
print()
# printing the elements without index
print("Printing the elements using while loop without index:")
print()
row = 0
while row in range(len(a)):
    if type(a[row]) is list:
        if len(a[row]) > 1:
            col = 0
            while col in range(len(a[row])):
                print(a[row][col])  # for index purposw we can write statement
                col += 1
            row += 1
    else:
        print(a[row])  # for index purpose we will write statement
        row += 1


# printing the elements with index
print()
print("Printing the elements using while loop with index:")
row = 0
while row in range(len(a)):
    if type(a[row]) is list:
        if len(a[row]) > 1:
            col = 0
            while col in range(len(a[row])):
                print("At row ", row, " and column ", col,
                      " the element is ", a[row][col])
                col += 1
            row += 1
    else:
        print("At row ", row, " the element is ", a[row])
        row += 1
print()
print("out of loop")

'''


# accessing the list having elements only as list
# all the elements of the lsit will be also a list
# accessing of this list element is easy, becuase here the type of all elememts are same . so we can easily accerss it

a1 = [34, 23, 34, "hello"]
a2 = ["harry", 343, 23, 134, "how"]
a3 = ["are", " you", 23, 134, ]
a = [a1, a2, a3]
print("The original list is ", a)
print("The length original list is ", len(a))
print()
print("The first list is ", a1)
print("The length of first list is ", len(a1))
print()
print("The second list is ", a2)
print("The length of second list is ", len(a2))
print()
print("The third list is ", a3)
print("The length of third list is ", len(a3))
print()
print("the elemets without index are")
# accessing the elements using while loop
# without index
row = 0
while row in range(len(a)):
    col = 0
    while col in range(len(a[row])):
        print(a[row][col])
        col += 1
    row += 1
print("out of looop")
print()

# with index
print("the elemets with index are")
row = 0
while row in range(len(a)):
    col = 0
    while col in range(len(a[row])):
        print("At row ", row, " and column ",
              col, " the value is ", a[row][col])
        col += 1
    row += 1
print("done man")
