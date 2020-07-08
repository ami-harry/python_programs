# arange function()
# it is used to create an array with a group of elements from start to one element prior to stop in steps of stepsize

# syntax
# numpy.arrange(start,end,stepsize,dtype=None)

# where
# start--> start of interval. the interval includes this value. the default value is zero
# end --> End of interval. the interval doesn't include this end value, except in some cases where step is an inter or float point round-off affects the length of out.
# we must have to  give end value. we cant avoid it.
# stepsize--> spacing between values. default value is 1.


# creating array using arange() function
# syntax
# import numpy
# arr=numpy.arange(start,end,stepsize)
# here start and step size can be avoided becuase start size is bydefault 0 and stepsize is 1. but we cant avoid end. we have to give it. and the output will always be less than end.

# arr=numpy.arange(5) -->here start is 0, stepsize is 1 and output will be 0 to 4
# arr=numpy.arange(1,5) -->here start is 1, stepsize is 1 and output will be 0 to 4
# arr=numpy.arrange(1,10,2) --> here start is 1, stepsize is 2 and output will be 1,3,5,7,9 only . till 10-1 means upto 9
# arr=numpy.arange(stop=5,step=1) this is invalid becuase if we are giving end and step size we must have to pass start value


"""
import numpy

arr = numpy.arange(15)
print("Value of first array which is arr=numpy.arrange(15) --> ")
for value in range(len(arr)):
    print("value at index no ", value, " is ", arr[value])

print("out of first loop")
print()

arr1 = numpy.arange(1, 15)
print("value of second array which is arr1 = numpy.arange(1, 15 ): --> ")
value1 = 0
while value1 in range(len(arr1)):
    print("value at index no ", value1, " is ", arr1[value1])
    value1 += 1
print("out of second loop")
print()


arr2 = numpy.arange(1, 15, 2)
print("value of third array which is arr2=numpy.arange(1,15,2): ")
for value2 in range(len(arr)):
    print("value at index no ", value2, " is ", arr2[value2])
print("out of third loop")
print()
exit(0)


"""

# taking input and printing the values

import numpy as hk
start_val = int(input("Enter the starting value: "))
stop_val = int(input("Enter the ending value: "))
step_val = int(input("Enter the step-size value: "))

array1 = hk.arange(start_val, stop_val, step_val)

for data in range(len(array1)):
    print("the value at index no ", data, " is ", array1[data])
