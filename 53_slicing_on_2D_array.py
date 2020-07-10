# slicing on 2D array can be useful to retrieve a piece of the array that contains a group of elements. slicing is useful to retrieve a range of elements
# syntax
# new_array=array_name[start:stop (this is row part)      :       stepsize,start:stop:step_size (this is column part)]
# the default start is 0
# the default stepsize is 1

# making a 2D array as per user demand and slicing on it

from numpy import *
row_size = int(input("Enter the row size for the array: "))
col_size = int(input("Enter the column size for the array: "))

array_2d = zeros((row_size, col_size), dtype=int)
print("The original array is \n", array_2d)

# getting input from the user
print("Enter ", (row_size*col_size), " elements for the array: ")
row_ele = 0
while row_ele in range(len(array_2d)):
    col_ele = 0
    while col_ele in range(len(array_2d[row_ele])):
        inp_data = int(input())
        array_2d[row_ele][col_ele] = inp_data
        col_ele += 1
    row_ele += 1
print()

print("The updated array is\n", array_2d)


start_pt_row = int(input("Enter the starting value for row"))
stop_pt_col = int(input("Enter the ending value for column"))
start_pt_col = int(input("Enter the starting value for column"))
stop_pt_row = int(input("Enter the ending value for row"))

arr = array_2d[start_pt_row: stop_pt_col, start_pt_col: stop_pt_row]
print(arr)
# a = array_2d[2, 1, 1:2, 1, 1]
# print(a)

# slicing on this array
# for slicing we make a new array in which we store the data extracted from the exisiting array
# we pass the parameter as start,stop and step size for row and col
# stop means n-1 means if stop size is 2 it will go upto 1


# in case of single value extraction we have to pass these range only once
# but if we want to access a range of both row and column then we have to pass these argments twice . once for row range and then for column range
# [0,:] --> means 0th row and all columns
# [:,1] --> means all rows and  0th columns
# array[0]--> means 0th row

# for specific element
# new_array=array[row_start:row_end, col_start:col_end]


# accessing range
# new_array= array[row_start:row_end, col_start:col_end]
#
# start_pt_row = int(input("Enter the starting value"))
# stop_pt_row = int(input("Enter the ending value"))
# start_pt_col = int(input("Enter the starting value"))
# stop_pt_col = int(input("Enter the ending value"))
#
#
# print("Enter the values to access a single element")
# new_arr = hk.array_2d[start_pt_row:stop_pt_row, start_pt_col:start_pt_col]
# print("Your element is ", new_arr)
#
#
