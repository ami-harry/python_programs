# attributes of numpy
# ndim
# this attribute represents the number of axes of the array. the number of dimensions is also referred as Rank.
# syntax ..array_name.ndim


# shape
# this attribute represents the shape of the array. the shape is a tuple listing the number of elements along each dimension.
# syntax ..array_name.shape

# size
# this attribute represents the total no of elements in the array
# syntax ..array_name.size

# itemsize
# this attribute represents the memory size of the array elements in the array
# syntax ..array_name.itemsize
#
# dtype
# this attribute represents the data type of elements in the array
# syntax ..array_name.dtype

# nbytes
# this attribute represents the total no of bytes occupied by elements of the array


# making 1D and 2D array

from numpy import *

size_1 = int(input("Enter the size :"))
one = zeros((size_1), dtype=int)
print(one)
print("Enter ", size_1, " elements for the array")
data = 0
while data in range(len(one)):
    inpu = int(input())
    one[data] = inpu
    data += 1

print("The array is \n", one)

row_size = int(input("Enter the row size: "))
col_size = int(input("Enter the col size: "))
two_d = zeros((row_size, col_size), dtype=int)
print(two_d)

print("Enter ", (row_size*col_size), " elements for the array:")
row_data = 0
while row_data in range(len(two_d)):
    col_data = 0
    while col_data in range(len(two_d[row_data])):
        input2 = int(input())
        two_d[row_data][col_data] = input2
        col_data += 1
    row_data += 1

print("the 2D array is \n", two_d)

print()
print("The ndim for one dimensional array is ", one.ndim)
print("The ndim for two dimensional array is ", two_d.ndim)
print("The shape of one dimensional array is ", one.shape)
print("The shape of two dimensional array is ", two_d.shape)
print("The size of one dimensional array is ", one.size)
print("The size of two dimensional array is ", two_d.size)
print("The item-size of one dimensional array is ", one.itemsize)
print("The item-size of two dimensional array is ", two_d.itemsize)
print("The dtype of one dimensional array is ", one.dtype)
print("The dtype of two dimensional array is ", two_d.dtype)
print("The nbytes of one dimensional array is ", one.nbytes)
print("The nbytes of dimensional array is ", two_d.nbytes)
