# passing array to function

'''
import array as hk  # importing array module as hk


# making a function and printing original array, type of array, and array elemnets as index no.
def arr_show(parameter):
    print(parameter)
    print(type(parameter))
    for elements in range(len(parameter)):
        print("Element at index no ", elements, " is ", parameter[elements])


my_array = hk.array('i', [23, 45, 23, 5, 234, 5])  # creating array
arr_show(my_array)  # passing the array as actual argument at function call

'''


'''
# passing array elemets to the function as per user input

from array import *

# function body


def my_fun(para):
    print()
    print("Printing the array elemets using the function")
    print("The original array elemets are: ", para)
    print("The type  is ", type(para))
    print()
    print("printing the array elements with index no :")
    for data in range(len(para)):
        print("The elemennt at index no ", data, " is ", para[data])


# making empty array and taking input by user
my_array = array('i', [])  # empty array
size_array = int(input("Enter the size of the array: ")
                 )  # asking the size of the array

# taking input using for loop
# for data in range(size_array):
#     my_array.append(int(input("Enter the array elements: ")))

# taking input using while loop
data = 0
while data in range(size_array):
    print("Enter the value for index no ", data, end='')
    # taking input for the array
    my_array.append(int(input(" ")))
    data += 1

# print("The original array is :", my_array)

# print("printing the array elemets using for loop")
# #
# for ele in range(len(my_array)):
#     print("Element at index no ", ele, " is ", my_array[ele])

# print('printing data using while loop')
# ele = 0
# while ele in range(len(my_array)):
#     print("Element at index no ", ele, " is ", my_array[ele])
#     ele += 1

# passing the  array to the function as actual paramter
my_fun(my_array)

'''