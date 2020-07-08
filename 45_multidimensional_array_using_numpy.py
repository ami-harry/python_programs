# multidimenstional array (2-D,3-D,4-D,----->n-D array)
# an array having more than one row and columns
# it is also called array of arrays

# this is 2-D array
# a=array([[10,20,30],
#           [40,05,20]])

# this is 3-D array
# a=array([[[1,2,3],
#           [3,5,6],
#           [54,34,23]]])

# this is 4-D array
# a=array([[[[1,2,3],
#           [2,4,6],
#           [34,54,23],
#           [34,34,23]]]])


# Methods for creating multidimensional array
# a.array() function
# b.zeros() function
# c.ones() function
# d.reshape() function
# f. arange() function. -->numpy.arange(start,end,step).reshape(row,col)

import numpy as name
import numpy as sh

one_d_array = sh.array([10, 230, 35, 34, 34])

two_d_array = sh.array([[23, 34, 34, 34],
                        [13, 14, 24, 74],
                        [73, 44, 34, 79]])


three_d_array = sh.array([[[[23, 54, 324, 54],
                            [45, 3, 56, 34, 5],
                            [5, 42, 23, 23, 23],
                            [45, 34, 34, 34, 3]]]])

four_d_array = sh.array([[[[23, 45, 34, 67],
                           [45, 34, 45, 23],
                           [45, 42, 4, 23],
                           [56, 45, 35, 34, ]]]])

five_d_array = sh.array([[[[[5, 67, 32, 67, 34],
                            [56, 67, 35, 2, 56]]]]])

# and so on

# print("Printing one-d array")
# print(one_d_array)
# print(one_d_array.dtype)
# print()
# print("Printing two-d array")
# print(two_d_array)
# print(two_d_array.dtype)
# print()
# print("Printing three-d array")
# print(three_d_array)
# print(three_d_array.dtype)
# print()
# print("Printing four-d array")
# print(four_d_array)
# print(four_d_array.dtype)
# print()
# print("Printing five-d array")
# print(five_d_array)
# print(five_d_array.dtype)
#
#
# print('before update')
# print(two_d_array)
# two_d_array[2][3]=500
# two_d_array[0][1]=500
# two_d_array[1][3]=500
# two_d_array[1][2]=500
# print('after update')
# print(two_d_array)
#
#

# index
# it represents the position of the element
# in multidimensional case, all the elements are collected in a sigle row, not in rows and column wise. yes, but their position will be in row and column and can be accessed throgh position number

# we can give float, int, string , list,dict etc as element

# name_array = name.array([["harry", "hariom", "ami-harry"],
                        #  ["Python", "java", "android"],
                        #  ["Mobile", "Laptop", "Desktop"]])
# 
# print(name_array)
# print(name_array.dtype)


# making two-dimensional array by users input
