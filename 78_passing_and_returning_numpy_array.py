from numpy import *
import numpy as hk
# passing and returning numpy array through function


'''

# 1. passing the array as a parameter and returning it from function
# from numpy import *


def show(ar):
    print("The original array passed in the function ", ar)
    print(type(ar))
    for data in ar:
        print(data)
    return ar


a = array([23, 4, 56, 34, 56, 32])
# passing array as parameter to the function and storing the reutrned array to variable
b = show(a)
print("the returned array", b)
print(type(b))
for i in b:
    print(i)

'''

'''
# passing the array to function and reutning it from function

# import numpy as hk


def show():
    a = hk.array([23, 4, 23, 56, 34])
    print("the original array in the function: ", a)
    for i in a:
        print(i)
    return a


b = show()  # stroing the returned array into a variable
print()
print("the returned array is ", b)
print(type(b))
for a in b:
    print(a)

'''

'''
# taking input the array and passing it into the function and printing the returned array:




# from numpy import *
def my_fun(ar):
    print("The array in the function passed in the function: ", ar)
    print(type(ar))
    for i in ar:
        print(i)
    return ar


# creating an empty array using numpy zeros
size_of_array = int(input("Enter the size of the array: "))
my_arr = zeros(size_of_array, dtype=int)

# taking input the array elements
for data in range(len(my_arr)):
    print("Enter the data for index no", data, end='')
    usr_inp = int(input(": "))
    my_arr[data] = usr_inp
print()
# this is the original array and we will pas this  array to the function as parameter
print("the original array is ", my_arr)

# calling the function and passing the array as parameter and storing the reurned array in variable

ret_arry = my_fun(my_arr)
print()
print("The returned from the function array is ", ret_arry)
print(type(ret_arry))
print()
for i in ret_arry:
    print(i)
'''


'''

# passing an empty array to the function and inserting the array elements by user input and print the value and returin the array and then after again print it


def my_fun(ar):
    print("the original array is in the function", ar)
    print(type(ar))
    for data in ar:
        print(data)

    # putting data in the recieved array as a parameter
    print("Taking input for the array inside the function")
    for inp in range(len(ar)):
        print("Enter the data for index no", inp, end='')
        usr_inp = int(input(": "))  # taking input from user
        ar[inp] = usr_inp  # putting the input into the arr using index
    print()
    print("The array after giving data to it", ar)
    print("Printing the array elements inside the function using index and value:")
    data = 0
    for data in range(len(ar)):
        print("value at index no ", data, " is ", ar[data])
    print()
    return ar


# asking the size of the array which is going to pass in the function
size_of_arr = int(input("Enter the size of the array: "))
# making an empty array and passing to function as a parameter
my_out_arr = zeros(size_of_arr, dtype=int)

print("the original array is at decleration time ",
      my_out_arr)  # array before passing it
print("Printing the original array using index and value:")
data = 0
while data in range(len(my_out_arr)):
    print("value at index no",data, " is ", my_out_arr[data])
    data += 1

print()
# passing the array and storing it into a variable
rec_arr = my_fun(my_out_arr)
print("The returned array from function is",
      rec_arr)  # printing the recieved array
print()
data = 0
for data in range(len(rec_arr)):  # printing the recieved array data using index
    print("value at index no ", data, " is ", rec_arr[data])
print()


'''


'''
# craeting an empty array in the function, taking input inside the function and returning it and priting it


def my_fun():
    arr_size = int(input("Enter the size of the array: "))
    my_array = zeros(arr_size, dtype=int)
    print("The original array in the function is  ", my_array)
    print()
    # giving data to it
    data = 0
    for data in range(len(my_array)):
        print("Enter data for index no", data, end='')
        usr_inp = int(input(": "))
        my_array[data] = usr_inp
    print("The updated array in the function is", my_array)
    print()
    return my_array


recieve = my_fun()  # storing the returned data from the function
# printing the returned function
print("The returned array from the function is  ", recieve)
print(type(recieve))
print("Printing the data using index and value:")
data = 0
while data in range(len(recieve)):
    print("Value at index no ", data, " is ", recieve[data])
    data += 1
print("Sucessfully printed")
print("Thanks for using it")
'''


'''
# returning an empty array from the function and assigning value outside the function and printing the data


def my_fun():
    size_of_arr = int(input("Enter the size of the array: "))
    my_arr = zeros(size_of_arr, dtype=int)
    print("The original array in the function is ", my_arr)
    return my_arr


rec_arr = my_fun()  # recieving the array returned by the function
print()
print("Array returned from function is is ", rec_arr)
print()
# giving data into it
data = 0
while data in range(len(rec_arr)):
    print("Enter the data for index no ", data, end='')
    usr_inp = int(input(": "))
    rec_arr[data] = usr_inp
    data+=1

print()
print("The updated array outside the function is ", rec_arr)
print()
print("Printing the array elements using index and value:")
data = 0
for data in range(len(rec_arr)):
    print("Value at index no ", data, " is ", rec_arr[data])
print('out of loops')
print('Thanks for using it')
'''

