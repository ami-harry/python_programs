# numpy built in function
# sum(arr) --> returns the sum of all the elements in the array
# prod(arr) --> returns the product of all the elements in the array
# sqrt(arr) --> returns square root value of the each element in the array

from numpy import *

a = array([25, 36, 49, 81], dtype=int)
b = array([[25, 36, 49, 81], [4, 16, 9, 144]], dtype=int)

# sum() function
print("The sum of a is ", sum(a))
print("The sum of b is ", sum(b))

# prod() function
print("The product of a is ", prod(a))
print("The product of b is ", prod(b))

# sqrt() function
print("The sqrt of a is ", sqrt(a))
print()
print("The sqrt of b is ", sqrt(b))

