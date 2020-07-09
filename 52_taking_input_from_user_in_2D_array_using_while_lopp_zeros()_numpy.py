# tking input in 2D array using for loop
# for taking input in 2D array
# firstly we will make an array with zeros
# we will manually set the dtype as int to get the values in int
# we will ask the user for the row and column after that using zeros function we will create the array
# accessing index we will enter the value to the array using loops
# and finally we will print the updated array

from numpy import *

row_size = int(input("Enter the size for row: "))
col_size = int(input("Enter the size for row: "))


# making the array as per input using zeros function
array1 = zeros((row_size, col_size), dtype=int)
print("The original array before modying the values")
print(array1)
print()

# taking input from user using while loop)
print("taking input from user using while loop")
row_data = 0
while row_data in range(len(array1)):
    col_data = 0
    while col_data in range(len(array1[row_data])):
        inp_data = int(input("Enter the elements: "))
        array1[row_data][col_data] = inp_data
        col_data += 1
    row_data += 1
print("out of loop")
print()


# printing the data using while loop
# a. without index
print("Printing elements using while loop without index")
row_data = 0
while row_data in range(len(array1)):
    col_data = 0
    while col_data in range(len(array1[row_data])):
        print(array1[row_data][col_data])
        col_data += 1
    row_data += 1
print("out of loop")
print()


# b. with index
print("Printing elements using while loop with index")
row_data = 0
while row_data in range(len(array1)):
    col_data = 0
    while col_data in range(len(array1[row_data])):
        print("The element at row", row_data, " and column ",
              col_data, " is ", array1[row_data][col_data])
        col_data += 1
    row_data += 1
print("out of loop")
print()


# printing the array elements using for loop
# a.without index
print("Printing elements using for loop without index")
row_data = 0
col_data = 0
for row_data in range(len(array1)):
    for col_data in range(len(array1[row_data])):
        print("The value at row ", row_data, " and column ",
              col_data, " is ", array1[row_data][col_data])
print("out of loop")
print()
print(array1)