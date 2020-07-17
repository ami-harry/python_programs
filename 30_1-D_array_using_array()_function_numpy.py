# array() function
# array() function of numpy module is use to create 1-D array
# syntax
# numpy.array(object,dtype=None,copy=True,order='K',subok=False,ndim=0)
# dtype is compulsory. python automatically detects the data type. we will give if we need type conversion.

# creating 1-D array using array() function.
# syntax
# import numpy
# array_Name=numpy.array([element])

# here array_name is the object for numpy class
# array is a function of numpy class

# 2nd method
# from numpy import *
# array_name=array([elements])
# by using * we have already imported all class and variable . so we dont need to mention that numpy class here .

# index
# an index represents the position of an array's element .
# we can acces elements by their index no
# we can update their values too by index no



import numpy

arr=numpy.array([10,20,40,59,54])
print("The array elements are " ,arr)
print("The data type of this array is ",arr.dtype)
print("Value of array at index no 0 is" ,arr[0])
print("Value of array at index no 1 is" ,arr[1])
print("Value of array at index no 2 is" ,arr[2])
print("Value of array at index no 3 is" ,arr[3])

# changing the data type of the array
# we add dtype in array as per our choice
# this is type conversion of array
arr=numpy.array([10,20,40,59,54],dtype=float)
# here all data are in int but we are changing the type forcefully.
# if any value is found in float then automatically it will be in float for saving the data loss
# this is done through explictly
print("\nThe data type of the array is ",arr.dtype)
print("The array elements are " ,arr)
print("Value of array at index no 0 is" ,arr[0])
print("Value of array at index no 1 is" ,arr[1])
print("Value of array at index no 2 is" ,arr[2])
print("Value of array at index no 3 is" ,arr[3])



print()
# this is implict data type. here python automatically changes the data type
arr=numpy.array([10.5,20,40,59,54])
print("The elements of array is " ,arr)
print("The data type of array is ",arr.dtype)
print("Value of array at index no 0 is" ,arr[0])
print("Value of array at index no 1 is" ,arr[1])
print("Value of array at index no 2 is" ,arr[2])
print("Value of array at index no 3 is" ,arr[3])

print()
arr=numpy.array(['h','a','r','i','o','m'])
print("The elements of array is " ,arr)
print("The data type of array is ",arr.dtype)
print("Value of array at index no 0 is" ,arr[0])
print("Value of array at index no 1 is" ,arr[1])
print("Value of array at index no 2 is" ,arr[2])
print("Value of array at index no 3 is" ,arr[3])
print()
# if we give index no which is not present in array then we will face an error or out of bound.
arr=numpy.array(["Harry","hariom","Mishti","Shalini","Keshav"])
print("The elements of array is " ,arr)
print("The data type of array is ",arr.dtype)
print("Value of array at index no 0 is" ,arr[0])
print("Value of array at index no 1 is" ,arr[1])
print("Value of array at index no 2 is" ,arr[2])
print("Value of array at index no 3 is" ,arr[3])
# in the output we will show a unique character <u1,2,3 like this
# this is showing the highest no of character of any string.

# updating value by index no
print("Before updating values")
print(arr)
arr[2]="Ishrat"
arr[4]="Kumar"
print("after updating values")
print(arr)
print("this is 1-D array using array() function of numpy")
print("thanks")


"""

# accessing array elemets using for loop
from numpy import *
arr = array([10, 20, 40, 60, 70])

print("printing values without using index ")
for data in arr:
    print(data)
print("out of loop")
print()

print("printing values  using index ")
for data in range(len(arr)):
    print("the value at index no ", data, " is ", arr[data])
print("out of loop")
print()
# accessing array elemets using while loop

data=0
while data in range(len(arr)):
    print("the value at index no ", data, " is ", arr[data])
    data += 1
print("out of loop")

"""

