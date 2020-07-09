# reshape() function
# this function is used to change the shape of any array. we can convert 1D array to 2D array or to 3D array and vice-versa. the new array should have the same number of elements in the original array.
# syntax
# new_array= reshape.(array_name,(n,r,c))
#
# where
# new_array-----> it is that array which is going to have the reshaped array.
# array_name---> it is that array which is going to convert.
# n --> no of array we want (mostly used in case of 3D array. while changing into 3D array we have to give that how many arrays we want).
# r is the no of rows
# c is the no of columns

# Converting 1D array to 2D array
"""

from numpy import *
array1 = array([1, 2, 3, 4, 10, 5, 6, 7, 8, 9])
# print(array1)

array2 = reshape(array1, (5, 2))
# be careful while giving no of rows and column
# print(array2)
print("The original 1D array \n", array1)
print()
print("The reshaped 2D array having 5 rows and 2 columns\n", array2)


"""

# Converting 1D array to 3D array
# to convert an 1D array to 3D array we must have atleast 9 elements. it will return 1 array of 3 having 3 rows and 3 column
# so for every 3d array having 3x3 we have to give 9 more elements
# or we can find simply by multiplying row X column to find the no of elements required.


from numpy import *
# creating 1D array to 3D array
# array1 = array([1,43,34,67,34,56,34,67,34,34,67,34,43,34,67,34,56,34,])
# array1 = array([43, 34, 67, 34, 56, 34, 67, 34, 34])
# array2 = reshape(array1, (1, 3, 3))
# here in case of 3D array,  1 means no of 3D array of 3X3 we want
# print("The original 1D array \n", array1)
# print("The reshaped 3 array of 3D array 3 rows and 3 columns\n", array2)
#

# creating 2D array to 3D array

# array1 = array([[1, 2, 3],
#                 [4, 5, 6],
#                 [7, 8, 9],
#                 [10, 11, 12],
#                 [13, 14, 15],
#                 [16, 17, 18]])

# array2 = reshape(array1, (3, 2, 3))

# print("the 2D array was \n", array1)
# print("The 3D array is \n", array2)

# creating 2D array to 1D array
# array1 = array([[1, 2, 3],
# [4, 2, 6]])
# array2 = reshape(array1, (6))
# here we simply pass an interger as no of elemets to be 1D array
# print("the 2D array was\n", array1)
# print("the 1D array is\n", array2)
#

# creating 3D array to 1D array

# array1 = array([[[132, 232, 233],
#  [345, 511, 334],
#  [535, 364, 342]]])
# array2 = reshape(array1, (9))
# print("the 3D array was\n", array1)
# print("the 1D array is\n", array2)
#

# simply for making any array into 1D array we can use flatten() method.
# this method is used to convert 2D or 3D array to 1D array.
# syntax
# arrayname.flatten()
array1 = array([[[132, 232, 233],
                 [345, 511, 334],
                 [535, 364, 342]]])
array2 = array([[651, 232, 533],
                [12, 322, 332],
                [41, 52, 323],
                [153, 242, 323]])

array3 = array1.flatten()
array4 = array2.flatten()
print()
print("The original array1 was in 3D\n", array1)
print()
print("modified 3D array in 1D form\n", array3)
print()
print("The original array2 was in 2D\n", array2)
print()
print("modified 2D array in 1D form\n", array4)
print()
print()
