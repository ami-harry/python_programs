# making an error as per uper input
# user will input the row and column size and how many arrays he wants to create using these inputs.. if the input arrys is of 2D then converting it into 3D.
# 2x3
# 6 elements

# minimun 4 elements are required to make an 2D array
# minimum 9 elements are required to make an 3D array
# if we have 9 elements, we can make an single 3D array of 3X3.

# Converting 1D array to 3D array
#

from numpy import *
size_of_array = int(input("Enter the no.of elements of 1-Darray: "))
arr1 = zeros(size_of_array, dtype=int)

# getting input in 1-d array
print("Enter ", size_of_array, " elements for 1-d array: ")
for data in range(len(arr1)):
    inp_data1 = int(input())
    arr1[data] = inp_data1
print("The 1D array is :")
print(arr1)



# getting input in 2d array

row_size = int(input("Enter the size of row for the 2D array : "))
col_size = int(input("Enter the size of column for the 2D array : "))
arr2 = zeros((row_size, col_size), dtype=int)

print("Enter ", (row_size*col_size), "elements for 2-d array: ")


row_data = 0
while row_data in range(len(arr2)):
    col_data = 0
    while col_data in range(len(arr2[row_data])):
        inp_data2 = int(input())
        arr2[row_data][col_data] = inp_data2
        col_data += 1
    row_data += 1

print("The 2D array is")
print(arr2)
