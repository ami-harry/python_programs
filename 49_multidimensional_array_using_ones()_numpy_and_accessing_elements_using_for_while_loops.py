# ones() function
# it is used to create 2d array with many rows and columns and all having 1.
# syntax.
# arr=ones(shape,dtype=float,order='C')


# creating 2-D array using ones()
import numpy as hk
my_array = hk.ones((3, 2))

# printing the data using index no
print(
    "the value at index no my_array[0][1] having default dtype float is ", my_array[0][0])
print(
    "the value at index no my_array[1][2] having default dtype float is ", my_array[1][1])
print(
    "the value at index no my_array[2][0] having default dtype float is ", my_array[2][0])

print()
print()
my_array1 = hk.ones((3, 2), dtype=int)
print(
    "the value at index no my_array1[0][1] having default dtype int is ", my_array1[0][0])
print(
    "the value at index no my_array1[1][2] having default dtype int is ", my_array1[1][1])
print(
    "the value at index no my_array1[2][0] having default dtype int is ", my_array1[2][0])
print()
# printing the data using for loop
# a. without index
print("Values using for loop without index: ")
for row_data in my_array:
    for col_data in row_data:
        print(col_data)

print("out of for loop for data without index")
print()

# a. with index
print("Values using for loop with index: ")
row_data = 0
col_data = 0
for row_data in range(len(my_array)):
    for col_data in range(len(my_array[row_data])):
        print("Value at row ", row_data, " and column ",
              col_data, " is ", my_array[row_data][col_data])

print("out of for loop for data with index")
print()

# printing the data using while loop
# a. without index
print("Values using while loop without index: ")
row_data = 0
while row_data in range(len(my_array)):
    col_data = 0
    while col_data in range(len(my_array[row_data])):
        print(my_array[row_data][col_data])
        col_data += 1
    row_data += 1

print("out of while loop for data without index")
print()

# b. with index
print("Values using while loop with index: ")
row_data = 0
while row_data in range(len(my_array)):
    col_data = 0
    while col_data in range(len(my_array[row_data])):
        print("Value at row ", row_data, " and column ",
              col_data, " is ", my_array[row_data][col_data])
        col_data += 1
    row_data += 1

print("out of while loop for data with index")
print()
print("Thanks for using ones() function")
