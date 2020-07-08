# logspace() function
# logspace() function is used to create an array with evenly spaced numbers logarithmatically. the sequence starts at bace **start(base to the power of the start) and ends with base **stop
# syntax
# numpy.logspace(start,stop,num=50,endpoint=True,base=10.0,dtyep=None,axis=0)

# where
# start --> it represents starting element which will become the power of the start. (base^start)
# stop --> it represents ending element which will become the power of the stop. (base^stop)
# num--> bydefault it is 50. it generally shows that in how many parts the array is goint to be divided.
# endpoint--> it takes the last element if it is True and will skip last value if it is False.
# base--> it is budefault 10. we can modify its value.
# dtype--> it is the data type of the array. bydefault it is None.

# syntax
# import numpy
# arr=numpy.logspace(start,stop,num=50,base=10.0, endpoint=True, dtype=None, axis=0)

"""

import numpy

arr = numpy.logspace(1, 3, 10)
# means it will take as from 10^1 to 10^3 and data will be in 10 parts
print('printing the data using for loop')
for data in range(len(arr)):
    print("At index no ", data, " the value is ", arr[data])

print('out of loop')
print()
print('printing the data using while loop')
data = 0
while data in range(len(arr)):
    print("At index no ", data, " the value is ", arr[data])
    data += 1

# changing the base
arr = numpy.logspace(1, 2, 10, base=5.0)
print('printing the data using for loop')
for data in range(len(arr)):
    print("At index no ", data, " the value is ", arr[data])

print('out of loop')
print()


"""


# taking input and generating the data
# input start value
# input end value
# input base value
# input num value


import numpy

inp_start = int(input("Enter the starting value: "))
inp_end = int(input("Enter the ending value: "))
inp_num = int(input("Enter the num value: "))
inp_base = float(input("Enter the base value: "))


arr = numpy.logspace(start=inp_start, stop=inp_end, num=inp_num, base=inp_base,endpoint=False)
print("printing the data using for loop")
for data in range(len(arr)):
    print("At index no ",data,"  the value is ",arr[data])
print("out of loop")
print("")

print("Printing the value using while loop: ")
data=0
while data in range(len(arr)):
    print("The value at index no ",data," is ",arr[data])
    data+=1
print("out of loop")

# here we can give anything as per our choice
# num means in how many parts the data items will be
# base means start and end value ka power