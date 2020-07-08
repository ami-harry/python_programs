# linspace() function
# linspace() function is used to create an array which evenly spaced number between a start and end point and stop point

# syntax
# numpy.linspace(start,stop,num=50,endpoint=True, ret-step=False, dtype=None,axis=0)
# this is bydefault.

# where
# start--> it represents starting element
# stop--> it represents ending element
# num--> it represents numbers of parts of the element should be divided . default is 50. it must be non-negative.
# endpoint--> if True , the array will accept the last element and for the False condiotion it will accept the value till n-1
# bydefault endpoint is True

# creating array using linspace() function
# syntax
# from numpy import *
# array_name=linspace(start,stop,num=50,endpoint=True)

# from numpy import *
# arr=linspace[1,8]
# here it means that an array will be created from 1 to 8 and will be divided into 50 equal blocks, becuase num value is bydefault is 50 and last value  will also be included becuase endpoint is bydefault True.

# arr=linspace(1,8,num=5)
# here 1 to 8 will be divided into 5 equal parts . here we have manually changed the num value.


#
#
# from numpy import *
#
# arr=linspace(1,15,num=30)
#
# for ele in range(len(arr)):
# print("value at index no ",ele," is ",arr[ele])
# print(arr.dtype)
# print('out of loop')

# print()
# print()
# arr=linspace(1,15,num=11,dtype=int)
# for ele in range(len(arr)):
# print("value at index no ",ele," is ",arr[ele])
# print('out of loop')
# print()
# print()

# arr=linspace(1,500,num=9,endpoint=False)
# for ele in range(len(arr)):
# print("value at index no ",ele," is ",arr[ele])
# print('out of loop')
# print()
# print()
#
# print('printing values using while loop')
# arr=linspace(1,5000,num=1009,endpoint=False)
# i=0
# while i in range(len(arr)):
# print("value at index no ",i," is ",arr[i])
# i+=1
#


# taking input from user and generating the data accoring to user using linspace() function


"""

import numpy

start_val = int(input("Enter the starting value: "))
end_val = int(input("Enter the ending value: "))
num_val = int(input("Enter the num value: "))

arr = numpy.linspace(start_val, end_val, num_val)
print("printing the data according to the input range using for loop: ")
for data in range(len(arr)):
    print("at index no ",data ,"value is ",arr[data])



print("printing the data according to the input range using while loop: ")
data=0
while data in range(len(arr)):
    print("at index no ",data ,"value is ",arr[data])
    data+=1

print("out of loop")
print("Thanks for using linspace() function")



"""
