# zeros() function
# this function is used to creat an array with all zeros
# syntax
# numpy.zeros(shape,dtype=float,order='C')

# where
# shape--> shape of new array. it can be an int which will represent members of elements or can be tuple of int. ex- 5,(5,),(3,1)
# dtype--> the desored data type for the array. bydefault it is float
# order --> whether to store multidimensional data in row-major (C style) or column-major(forton style) order in memory. it can be C or F. bydefault it is C


"""
import numpy as hk
arr = hk.zeros(5)
# this will give 0.0 for 5 times. becuase bydefault it is float
for data in range(len(arr)):
    print("Value at index no ", data, " is ", arr[data])
print(arr.dtype)
print("out of loop")
print()


arr1 = hk.zeros(5, dtype=int)
# this will give 0 for 5 times. becuase we have changed dtype to int
data = 0
while data in range(len(arr1)):
    print("Value at index no ", data, " is ", arr1[data])
    data += 1
print(arr1.dtype)
print("out of loop")
print()

# multi-dimensional array
arr2 = hk.zeros((3, 5,3)) #here 2 is the size or start or index no,five is the rows of th array or matrix and is the column of the matrix . this means 2,5,3 is 4X3 (4 row and 3 column) matrix which will be print two times for index 0 and 1
data = 0
while data in range(len(arr2)):
    print("Value at index no ", data, " is ", arr2[data])
    data += 1

"""
