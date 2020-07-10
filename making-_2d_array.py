# making 2-D array

import numpy as hk

row_size = int(input("Enter the row size: "))
col_size = int(input("Enter the column size: "))

array_2D = hk.zeros((row_size, col_size), dtype=int)
print("The original array is \n", array_2D)

# taking input using for loop
# print("\nEnter ", (row_size*col_size), " elements for the array")
# for row_ele in range(len(array_2D)):
#     for col_ele in range(len(array_2D[row_ele])):
#         inp_ele = int(input())
#         array_2D[row_ele][col_ele] = inp_ele
# print("out of input loop")
# print()

# taking input using while loop
print("Enter ", (row_size*col_size), " elements for the array ")
row_ele = 0
while row_ele in range(len(array_2D)):
    col_ele = 0
    while col_ele in range(len(array_2D[row_ele])):
        inp_data = int(input())
        array_2D[row_ele][col_ele] = inp_data
        col_ele += 1
    row_ele += 1
print()


print("\nPrinting the array elements with row and column using for loop")
row_ele = 0
col_ele = 0
for row_ele in range(len(array_2D)):
    for col_ele in range(len(array_2D[row_ele])):
        print("Value at row ", row_ele, " and column ",
              col_ele, " is ", array_2D[row_ele][col_ele])
print()
print()


print("\nPrinting the array elements with row and column using while loop")
row_ele = 0
while row_ele in range(len(array_2D)):
    col_ele = 0
    while col_ele in range(len(array_2D[row_ele])):
        print("Value at row ", row_ele, " and column ",
              col_ele, " is ", array_2D[row_ele][col_ele])
        col_ele += 1
    row_ele += 1
print()
print()


print("Printing the updated array\n", array_2D)
