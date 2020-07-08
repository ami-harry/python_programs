# accessing 2-D array elements using while loop(nested while loop)

# the outer while loop will be pointing rows and inner will be pointing columns.


import numpy as mi
my_array = mi.array([[23, 634, 923, 342],
                     [35, 34, 38, 24],
                     [35, 1234, 3453, 24],
                     [3435, 234, 23, 2344],
                     [235, 3534, 33, 3247],
                     [3435, 364, 653, 2412],
                     [355, 4634, 573, 2464], ])

"""
print("the original array is \n", my_array)
# this will print the original array
print()
# this will print the data of 0th row
print("the data at my_array[0]\n", my_array[0])
# this will print the data at 1th row
print()
print("the data at my_array[1]\n", my_array[1])
# this will print the rows data
# this will print the data at 0th row and 0th column
print()
print("the data at my_array[0][0]\n", my_array[0][0])
# this will print the data at 0th row and 1th column
print()
print("the data at my_array[0][1]\n", my_array[0][1])
# this will print the data at 1th row and 0th column
print()
print("the data at my_array[1][0]\n", my_array[1][0])
# this will print the data at 1th row and 1th column
print()
print("the data at my_array[1][1]\n", my_array[1][1])

"""

# accessing the elements
# a. without index
# b. with index


# printing the original array
print('the original array is:')
print(my_array)
print()


# a. without index
print("the array elements without index")
row_data = 0
while row_data in range(len(my_array)):
    col_data = 0
    while col_data in range(len(my_array[row_data])):
        print(my_array[row_data][col_data])
        col_data += 1
    row_data += 1
    print()
print('out of loop')
print("Out of while loop for without index values")
print()

# b. with index
print()
print("the array elements with index")
row_data1 = 0
while row_data1 in range(len(my_array)):
    col_data1 = 0
    while col_data1 in range(len(my_array[row_data1])):
        print("The value at row ", row_data1, " and column ",
              col_data1, " is ", my_array[row_data1][col_data1])
        col_data1 += 1
    row_data1 += 1
    print()
print("out of loop")
print("Out of while loop for with index values")
print()


# accessing the data using for loop
print("accessing the data using for loop")
print("without index value are")

for r_data in range(len(my_array)):
    for c_data in range(len(my_array[r_data])):
        print(my_array[r_data][c_data])
    print()
print("Out of for loop for without index values")
print()
print()
print("with index value are")
for ro_data in range(len(my_array)):
    for co_data in range(len(my_array[ro_data])):
        print("the value at row ", ro_data, " and column ",
              co_data, " is ", my_array[ro_data][co_data])
    print()

print("out of for loop for without index values")
print("Thanks for using this one")
