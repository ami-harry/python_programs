# where() function
# this function is used to create a new array which contains returned element choosen from exp1 or exp2 depending upon the given condition. if condition is true then exp1 is executed else exp2

# syntax
# numpy.where(condition, exp1,exp2)

import numpy as hk
array1 = hk.array([40, 10, 560, 5440, 1334, 45, 30, 560, 5440])
array2 = hk.array([201, 30, 50, 4450, 334, 45, 50, 334, 452])

print()
print("Array1 elements are")
print(array1)
print()
print("Array1 elements are")
print(array2)
print()
print("From where the element of array1 is greater than element of array2")
array3 = hk.where(array1 > array2, "hi","hello")
print(array3)
print()
print("From where the element of array1 is less than element of array2")
array3 = hk.where(array1 < array2, "harry","hariom")
print(array3)
print()
print("From where the elements of array1 are equal to elements of array2")
array3 = hk.where(array1 == array2, array1, array2)
print(array3)
print()

# it returns the arrays by comparing every index based on codition.
# if condition is matched then first statement is return else second
# we can give anything on statement. string, int, float, bool etc

