# zeros() fucntion for multidimensional array
# zeros() function is used to create 2D array with all zeros.
# syntax
# numpy.zeros(shape,dtype=float,order='C')

# creating 2_D array using zeros()

"""
from numpy import *

array1 = zeros((3, 2))
print("this will give output as all zero in the array in floating value becuase its bydefalut value is float")
print(array1)
print("The data type of this array is ", array1.dtype)
print()
array1 = zeros((3, 2), dtype=int)
print("This time the output will be in int form")
print(array1)
print("The data type of this array is ", array1.dtype)

# here in zeros((row,col)), we pass the parameter in this form
# and it takes as 0 to n-1 value

"""
# accessing array elements

import numpy as hk
my_array = hk.zeros((4, 5))

# we can print the elements index by index and can modify the values thorugh index no

# printing the values using for loop
# a.with index
# b.without index


# a with index
print("Printing elements with index no using for loop")
for row in range(len(my_array)):
    for col in range(len(my_array[row])):
        print("Element at row ", row, " and ",
              col, " is ", my_array[row][col])
    print()
print("Out of loop")

# b.without index
print("Printing elements without index no using for loop")
row = 0
col = 0
for row in my_array:
    for col in row:
        print(col)
    print()
print("Out of loop")
print()

# accessing the elements using while loop
# a.without index
print("Printing elements with index no using while loop")
row = 0
while row in range(len(my_array)):
    col = 0
    while col in range(len(my_array[row])):
        print("Element at row ", row, " and col ",
              col, " is ", my_array[row][col])
        col += 1
    row += 1
    print()
print("out of loop")
print()
# a.without index
print("Printing elements without index no using while loop")
row = 0
while row in range(len(my_array)):
    col = 0
    while col in range(len(my_array[row])):
        print(my_array[row][col])
        col += 1
    row += 1
    print()
print("out of loop")
