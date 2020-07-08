# ones() function
# ones() function is used to create an array with all 1s.

# syntax
# numpy.ones(Shape,dtype=float,order='C')

"""

import numpy as hk
arr = hk.ones(5)
# this will give 0.0 for 5 times. becuase bydefault it is float
for data in range(len(arr)):
    print("Value at index no ", data, " is ", arr[data])
print(arr.dtype)
print("out of loop")
print()


arr1 = hk.ones(5, dtype=int)
# this will give 0 for 5 times. becuase we have changed dtype to int
data = 0
while data in range(len(arr1)):
    print("Value at index no ", data, " is ", arr1[data])
    data += 1
print(arr1.dtype)
print("out of loop")
print()

# multi-dimensional array
# here 2 is the size or start or index no,five is the rows of th array or matrix and is the column of the matrix . this means 2,5,3 is 4X3 (4 row and 3 column) matrix which will be print two times for index 0 and 1
arr2 = hk.ones((3, 5, 3), dtype=int)
data = 0
while data in range(len(arr2)):
    print("Value at index no ", data, " is ", arr2[data])
    data += 1

"""
