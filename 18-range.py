# range()
# range() function is used to generate a sequence of integers starting from 0 bydefault and incerements the value by 1 bydefault , till j-1
# range(start, stop, stepsize)
# start-> starting position. uf we do not mention start its by default from 0
# **stop->ending position. the range of integer stops one element prior to stop. if stop is j then it will stop at exact j-1.
# stepsize--> increment by stepsize. if we do not mention start by default it increases the value by 1

# rules
# --> all arguments must be inteegr, wether +ve or -ve
# you can not pass a string or float number or any other type in start, stop or stepsize
# the stepsize value should not be zero


# with only one argument(stop) from 0 to stop-1
# a = range(10)
# here we are not mentioning the starting value
# so it will begin from 0 to 9 .meanwhile j-1(stop value -1)
# print('a[0] is', a[0])
# print('a[1] is', a[1])
# print('a[2] is', a[2])
# print('a[3] is', a[3])
# print('a[4] is', a[4])
# print('a[5] is', a[5])
# print('a[6] is', a[6])
# print('a[7] is', a[7])
# print('a[8] is', a[8])
# print('a[9] is', a[9])
# print()
# print("now printing the values using loop")
# for b in a:
# print(b)
#
# print("we have printed values using loop")

# with 2 arguments(start, end) starting value and end-1
# a = range(1, 10)
# here we have given starting value
# so it will start from 1 and will go upto 9
# print('a[0] is ', a[0])
# print('a[1] is ', a[1])
# print('a[2] is ', a[2])
# print('a[3] is ', a[3])
# print('a[4] is ', a[4])
# print('a[5] is ', a[5])
# print('a[6] is ', a[6])
# print('a[7] is ', a[7])
# print('a[8] is ', a[8])
# print()
# print("now printing the values using loop")
# for b in a:
    # print(b)
# 
# print("we have printed values using loop")
# 

# with 3 arguments (start,end, step)
# a=range(2,50,2)
# it will start from 2 and will goto 50 and will increase the  value by 2
# for b in a:
    # print(b)
# print("we have pronted the values using for loop")

# from 10 to 1. reverse order
# a=range(10,0,-1)
# for b in a:
    # print(b)


