# aliasing array
# aliasing means giving a nickname for the existing object. it doesn't mean that we are copying.
# both will be tagged with the same memory location.
# both a and b will return the same data.
# but we cant say that we have copied the data of a into b
# it is showing same data becuase it is also tagged with the same location as well.

import numpy as hk
array1 = hk.array([234, 45, 3, 54, 56, 57, 67, 45, 43, 3])
array2 = array1

print("Elements of array1 is ", array1)
print("Elements of array2 is ", array2)

print("memory location of array1 is ", id(array1))
print("memory location of array2 is ", id(array2))
