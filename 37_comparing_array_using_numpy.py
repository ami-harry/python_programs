# relational and comparison operators
# relational operators are used to compare the value of operands(expressions) to produce a logical value. a logical value is either True of False
# [<    >   <=   >=  ==     !=]

# comparing array using numpy
# comparision operation can be used to compare arrays. the size of the array must be same. comparison operators compares the corresponding elements of the arrays  and returns another array with boolean values.

import numpy as hk

array1 = hk.array([100, 200, 400, 4534, 5634, 45, 23, 400, 4534, 400, 4534, ])
array2 = hk.array([400, 543, 23, 44, 344, 45, 23, 876, 523, 44, 344])
print("array1 element is")
print(array1)
print()
print("array2 element is")
print(array2)
print()

print("Sum of elements of array1 and  array2 ")
array3 = array1 + array2
print(array3)
print()

print("which elements of array1 is greater than elements of array2")
array3 = array1 > array2
print(array3)
print()

print("which elements of array1 is less than elements of array2")
array3 = array1 < array2
print(array3)
print()

print("is elements of array1 and  array2 are equal")
array3 = array1 == array2
print(array3)
print()
