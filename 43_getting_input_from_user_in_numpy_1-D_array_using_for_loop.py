# getting input from the user for 1-d array using numpy methods
# getting input using for loop

# here we are making an array of zero zero oof n blocks using zeros method.

"""

from numpy import *
a = zeros(5)
print("Original array returned by zeros function ")
print(a)

# this will create an array of 5 blocks of having zero only becuase of zeros function.
# we will ask the user for the size of the array
# and we will modify the value of array using their index which is returned by the zeros function.
# using loop we will access the index of the array and will modify the value.

size_of_array = int(input("Enter the size of the array: "))
a = zeros(size_of_array, dtype=int)
# here we are changing the data type of array to int, bydefault it is float

# range(len(a)) --> this will return the length of the array , this will help to access the array index using loops, size_of_array is the length of the array.s


# assigning the data
for data in range(len(a)):
    inp = int(input("Enter the data for array: "))
    a[data] = inp

print("We have updated array")
print()

# here we are storing the input in inp variable which is entered by the user
# and then we are assigning that value wth index of the array
# printing the modified array elements

print("Printing modified array")
data = 0
for data in range(len(a)):
    print("The array element at index no ", data, " is ", a[data])

print("out of loop")


"""

import numpy as hk

# now taking input the size of the array and the array elements from user and printing the array

size_of_array = int(input("Enter the size of the array:"))
array = hk.zeros(size_of_array, dtype=int)

print()
print("The original array returned by the zeros function for the size you have enetered is :  ", array)
print("Modifying values through index ")

for element in range(len(array)):
    inp_by_user = int(input("Enter the array elements : "))
    array[element] = inp_by_user

print()
print("The modified array elements are :")
data = 0
for data in range(len(array)):
    print("The value at index no ", data, " is ", array[data])

print('out of loop')
