# array
# in python , array is an object that provide a mechanism for storing several data items with only one identifier thereby simplifying the task of data managaemnt. array is benefecial if we need to store group of elements of same data type. in Python , array can increase or decrease their size dynamically.
# ex-group of students, group of employees, group of integers, group of floats
# array can store only one type of data
# in python, the size of array is not fixed. array can increase or decrease their size dynamically
# array and list are not same
# array ues less momory than list

# why we need array :/
# if we have to store roll no of 10 students we have to make 10 different variable and have to store every data in every variable
# and accessing every data by print statement is quite difficult. so we need an array for making or task easy

# ex- 101,102,103,104,105
# here we are storing the data in a single variable

# st1_roll=101
# st2_roll=102
# st3_roll=103
# st4_roll=104
# st5_roll=105

# here we are accessing the data one by one and it is very difficult

# print(st1_roll)
# print(st2_roll)
# print(st3_roll)
# print(st4_roll)
# print(st5_roll)


# we can make our task much easir by using array
# we can store same data as follow and access

# st_roll = ([101, 102, 103, 104, 105])
# st_roll = ('i',[101, 102, 103, 104, 105])
# for roll in st_roll:
# print(roll)


# types of array

# one dimensional array/1-D array
# (single row- multiple columns)
# ex-[101,102,103,104,105]

# multi-dimensional array
# (multiple row and multiple columns)
# ex-
# [50,60,70,26,57]
# [40,20,90,16,47]
# [50,60,70,26,57]
# [40,20,90,16,47]
# here we are storing marks of students of different subject

# note- python does not support multi-dimensional array but we can create multi-dimensional array using third party package like Numpy

# To use array, we have to import array module in python program.
# we have two methods through which we can import array module

#  import array
#  this will import entire array module

# from array import *
# this will import all class, objects, variable etc from array module. hence * means all

# creating and initialzing 1-D array
# 1. syntax
# import array -->this is module

# array_name=array.array('type_code',[elements])
# here array_name can be any variable in which we are holding the array elements (it is also called object of class array)
# first array is module name
# second array is a class named as array in array module
# . means (an array class of array methods)


# from array import *
# array_name = array('type_code, [elements])
# here array_name can be any variable in which we are holding the array elements (it is also called object of class array)
# array is the class name

# we can give a nickname for our modules while importing that module for our simplicity
# import array as hk
# here hk is now the module and we can use it behalf of module name
# array_name= hk.array('type_code,[])
# here hk is module name and array is the class of module hk and array name is the object for array class

# creating empty 1-D array
# from array import *
# array_name=array('i',[])

# this is called empty array in which we wll take input from user and will hold the data

# type codes for array

# Type_code --> C-Type          --> Python-type     --> Size

#    b  --> signed char         --> int             -->   1
#    B  --> unsigned char       --> int             -->   1
#    h  --> signed short        --> int             -->   1
#    H  --> unsigned short      --> int             -->   1
#    i  --> signed int          --> int             -->   1
#    I  --> unsigned int        --> int             -->   1
#    l  --> signed long         --> int             -->   1
#    L  --> unsigned unsigned   --> int             -->   1
#    q  --> signed long float   --> int             -->   8
#    Q  --> signed long float   --> int             -->   8
#    f  --> float               --> int             -->   4
#    d  --> duble               --> float           -->   8

# there is no type for char and string in python
# we have to use numpy for that purpose

# index
# an index represents the position number of an array's element
#
# from arrray import *
# st_roll=array('i',[101,102,103,104,104])

# index always starts from 0 to n-1
# python interpreter allocates n blocks of memory and store the elements with index no 0 to n-1

# to access the array elemets we can access through their index no

# import array
# st_roll= array('i',[101,102,103,104,105])
# or
# from array import *
# st_roll= array('i',[101,102,103,104,105])

# or we can give a nickname for our module name
# import array as hk
# st_roll = hk.array('i', [101, 102, 103, 104, 105])

# here hk is now the module name for array and we can use it

# print('value at index no st_roll[0]', st_roll[0])
# print('value at index no st_roll[1]', st_roll[1])
# print('value at index no st_roll[2]', st_roll[2])
# print('value at index no st_roll[3]', st_roll[3])
# print('value at index no st_roll[4]', st_roll[4])

# using for loop we are accessing the array elements
# import array as hk
# st_roll = hk.array('i', [101, 102, 103, 104, 105])
# i=0
# for h in st_roll:
# print('value at index no',i,h)
# i+=1

# type conversion
# array elements automatically detects the type conversion
# suppose if out type code is float and by mistake if we give integer data to it then it will be changed into float
# but for interger type code the float value can't be changed into int becuase here we will loss our data. so be careful

# int can be changed into flaot
# but float values can't be changed into int

# ####################################################################
# import array as hk
#
# st_roll=hk.array('i',[10,10.50,11,12.53,40])
# i=0
# for data in st_roll:
# print("data at index no",i,data)
# this will give an error becuase our type code is integer and we are giving float values in  it .so it will not run

# ####################################################################

# import array as hk
# st_roll=hk.array('f',[10,10.50,11,12.53,40])
# i=0
# for data in st_roll:
# print("data at index no",i,data)

# here the integer values will be converted into float bydefault.


# accesing elements using for loop
# we can print elements by knowing the lengh of the array
# we can also use range function

# this is with index
# from array import *
# st_roll = array('i', [13, 12, 543, 654, 755, 86, 37, 78, 39, 210])
# n = len(st_roll)
# n will store the lenght of the array st_roll
# for i in range(n):
# print('value at index no', i, '=', st_roll[i])
# print('we are out of loop')

# without index
# from array import *
# st_roll = array('i', [13, 12, 543, 654, 755, 86, 37, 78, 39, 210])
# for i in st_roll:
# print(i)
# here only array elements will be on the console


# accesing array elements using while loop
# from array import *
# st_roll = array('i', [13, 12, 543, 654, 755, 86, 37, 78, 39, 210])
# n = len(st_roll)
# i = 0
# i must be start from 0 becuase of index no...otherwise we will be facing error
# while (i < n):
# print('value at index no',i, '=',st_roll[i])
# i += 1
# print('out of loop')


# append()
# this method is used to add an element in the existing element at the last.
# only one element can be added in the array by append

# from array import *
# st_roll = array('i', [13, 12, 543, 654, 755, 86, 37, 78, 39, 210])
# n = len(st_roll)
# i = 0
# i must be start from 0 becuase of index no...otherwise we will be facing error
# while (i < n):
# print('value at index no', i, '=', st_roll[i])
# i += 1
# print('out of loop and adding elements using append')
#
# st_roll.append(199)
# st_roll.append(201)
# st_roll.append(204)
# n = len(st_roll)
# i = 0
# print('after appending values the array elements are')
# i must be start from 0 becuase of index no...otherwise we will be facing error
# while (i < n):
# print('value at index no', i, '=', st_roll[i])
# i += 1
# print('out of loop')
# we have added three values in the end using append method in the array

#
# ***************** taking input to array from user using for loop******************************

# to take input from user we must have some important concepts to be clear
# know how to take input form user
# how append method works
# how range and length method works
# know about the loops to take input and show the values
#
# first of all we will make an empty array , then we will ask user about the size of the array
# then we will run a loop and takes input from user and will keep it in array using append method
# after storing elements we will again run a know the range of the array for index purpose
# after that we will print the array elements

# from array import *
# std_roll = array('i', [])  # this is an empty array
# here we are asking the size of the array
# n = int(input("enter the size of the array: "))
# for i in range(n):  # here we are generating the range after knowing the size
# here we are asking the user to give input for the array. here the append method will take the inputs into the array one by one. here we are typecasting the input into int becuase bydefault the input function take input as string.
# std_roll.append(int(input('enter the elements: ')))
# print()
# print('printing array elements')
# print()
# now printing the array elements
# for i in range(len(std_roll)):  # here after adding the elements we are cheching the length of the array and generating the range for indexing purpose
# print('value at index no', i, '=', std_roll[i])
# print('out of loop or the array elemets are printed sucessfully')


# ***************** taking input to array from user using while loop*****************************
# from array import *
# std_roll = array('i', [])  # this is an empty array
# n = int(input("enter the size of the array: "))
# i=0
# while (i<n):
# std_roll.append(int(input('enter the elements:')))
# i+=1
# print()
# print('printing array elments')
# print()
# i=0 # here we have initialize i=0 again becuse i was inceased while taking input. we can take another variable here.
# while (i<len(std_roll)):
# print('value at index no',i,'=', std_roll[i])
# i+=1
# print('out of loop')
#
#
# ****taking input using while loop and accessing elements using for loop******
# from array import *
# std_roll = array('i', [])  # this is an empty array
# print('taking input elements using while loop')
# n = int(input("enter the size of the array: "))
# i=0
# while (i<n):
# std_roll.append(int(input('enter the elements:')))
# i+=1
# print()
# print('printing array elments using for loop')
# print()
# for i in range(len(std_roll)):
# print('value ar index no',i,'=', std_roll[i])
# print('out of loop')


#  ****taking input using for loop and accessing elements using while loop******

# import array as hk
# std_roll=hk.array('i',[])
# print('taking input using for loop\n')
# size=int(input('enter the size of the array: '))
# for i in range(size):
# std_roll.append(int(input('enter the array elements:')))
# print()
# print('printing values using while loop')
# print()
# i=0
# while (i<len(std_roll)):
# print('value at index no',i,'is',std_roll[i])
# i+=1
# print('out of loop')
#
#
# ************insert() method*****************
# this method is used to insert an element in a particular position of existing array
# syntax
# array_name.insert(positio_no, new_element)

# from array import *
# std_roll = array('i', [10, 20, 30, 40, 50])
# n=len(std_roll)
# i=0
# while (i<n):
    # print('value at index no',i,'is',std_roll[i])
    # i+=1
# print()
# print('value after inserting elements')
# print()
# 
# std_roll.insert(2,5)
# std_roll.insert(4,15)
# std_roll.insert(6,25)
# n=len(std_roll)
# i=0
# for i in range(n):
    # print('value at index no', i, 'is', std_roll[i])
# # print('out of loop')


