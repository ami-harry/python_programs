# mathematical operations on arrays using numpy
# we can perform mathematical operations like addition, substraction, mulltiplication ,division etc on the element of an array. math functions from the math module can also be possible to apply to the elements of the array

import numpy as hk

# array1 = hk.array([20, 40, 34, 64, 35, 34])
# print("Original array elements")
# print(array1)
# print()
# print("Updated array elements")
# array1 += 20
# this means every value will be increase by 20 this time
# print(array1)

array2 = hk.array([54, 67, 23, 56, 342, 56])
array3 = hk.array([20, 40, 34, 64, 35, 34])

print(array2)
print(array3)
print()
print("The sum of array2 and array3 is: ")
print(array2+array3)
print()
print("The substraction of array2 and array3 is: ")
print(array2-array3)
print()
print("The multiplication of array2 and array3 is: ")
print(array2*array3)
print()
print("The division of array2 and array3 is: ")
print(array2/array3)
print()
print("The remainder of array2 and array3 is: ")
print(array2 % array3)
print()
print("The square array2 elements is: ")
print(array2*array2)
print()
print("The cube array2 elements is: ")
print(array2*array2*array2)
print()
print("The square array3 elements is: ")
print(array3*array3)
print()
print("The cube array3 elements is: ")
print(array3*array3*array3)
print("value of array1 are greater or not in array2 at same index ")
print(array2>array3)



