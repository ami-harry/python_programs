# tking input in 2D array using for loop
# for taking input in 2D array
# firstly we will make an array with zeros
# we will manually set the dtype as int to get the values in int
# we will ask the user for the row and column after that using zeros function we will create the array
# accessing index we will enter the value to the array using loops
# and finally we will print the updated array

#
import numpy as hk

# taking input from the user
row_size = int(input("Enter the size for row: "))
col_size = int(input("Enter the size for row: "))

# making the array as per input using zeros function
array1 = hk.zeros((row_size, col_size), dtype=int)
print("The original array before modying the values")
print(array1)
print()

# asking the value from user and modifying the array using index
for row in range(len(array1)):
    for col in range(len(array1[row])):
        inp_data = int(input("Enter the elements: "))
        array1[row][col] = inp_data
print()

# printing the array using for loop

# a. with index
print("printing the array using for loop with index: ")

for row_data in range(len(array1)):
    for col_data in range(len(array1[row_data])):
        print("The element at row ", row_data, " and column ",
              col_data, " is ", array1[row_data][col_data])
print("out of loop")

# printing the array using for loop
# b. without index
print("printing the array using for loop without index: ")

for row_data1 in range(len(array1)):
    for col_data1 in range(len(array1[row_data1])):
        print(array1[row_data1][col_data1])
print("out of loop")
print()


# printing the array using while loop
# a. without index
print("printing the array using while loop without index: ")
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
print("printing the array using while loop with index: ")
row_data1 = 0
while row_data1 in range(len(array1)):
    col_data1 = 0
    while col_data1 in range(len(array1[row_data1])):
        print("The element at row ", row_data1, " and column ",
              col_data1, " is ", array1[row_data1][col_data1])
        col_data1 += 1
    row_data1 += 1
print("out of loop")
print()
print(array1)