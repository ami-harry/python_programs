# accessing the array elements using for loop

# we will make an 2-d array using for loop

# length of an 2-d array is just the no of rows of the array
# we will use nested for loop to extract data of array .
# outer for loop will represents the rows and the inner loop represents the column in each row
# the data will be filtered using ith . from every ith row the jth column data will be extract
#

import numpy as shalini
my_array = shalini.array([[10, 20, 30, 40],
                          [1, 2, 3, 4]])


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

# accessing data using for loop
# a. without index
# b. with index

# a. without index
print("Values without index:")
for row_data in my_array:
    for col_data in row_data:
        print(col_data)
    print()
# this will give all the data

# b. with index
print("Values with index:")
for row_data1 in range(len(my_array)):
    for col_data1 in range(len(my_array[row_data1])):
        print("The value at row ", row_data1, " and column ",
              col_data1, " is ", my_array[row_data1][col_data1])
    print()
print("Out of loop")
