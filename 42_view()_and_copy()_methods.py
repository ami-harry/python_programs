# view() function
# this method is used to construct a new view of an array with same data of the existing array. the esisting array and the new array will share different memory location
# while sharing different memory locations no matter. if we made change in any one then it will effect on both arrays.
# it is just like mirror effect
"""

from numpy import *
a = array([34, 46, 314, 56, 45, 2, 24, 344])
b = a.view()
# now  b is the mirror effect of a
# b is viewing like a
# but both have different memory locations
print(a)
print(b)
print()
print("The memory location of a is ", id(a))
print("The memory location of b is ", id(b))

# updating a value
a[2] = 500
# this will effect both and b
print()
print("value after updating a[2]=500")
print(a)
print(b)

print()
# updating b value
b[3] = 23212
# this will effect both and b
print("value after updating b[3]=23212")
print(a)
print(b)

"""

# copy() method
# this method is used to create a copy of an existing array. if the new array gets modified the oter will not get effected. both will share different memory locations. there is no connection between the existing and the copied array

from numpy import*
a = array([45, 5, 34,2234, 2, 324, 22, 32, 34, 32, 23])
b = a.copy()
# here b is the copy of a
# both have same value now and different memory location
# if a is modified then b will not be affected and vice-versa

print("Original values")
print("a = ", a)
print("b = ", b)

print("The memory location of a is ", id(a))
print("The memory location of b is ", id(bartlett))
print()

# updating a value
a[5] = 50
print("Values after modification as a[5]=50 ")
print("a = ", a)
print("b = ", b)
print()

b[6] = 234
print("Values after modification as b[6]=234 ")
print("a = ", a)
print("b = ", b)
print()
