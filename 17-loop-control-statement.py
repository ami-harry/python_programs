# loop control statement are used when a section of code may either be executed a fixed no of times or while some condition is true.
# while
# for

# while
# the while loop keepds repeating an action until an associated condition returns fasle.

# a = 2
# while a <= 10:
# print(a)
# a += 2
# print("next line")
# b = 1
# while b <= 10:
# print(b)
# b += 1
# print("next line")

# a=int(input("Enter the initial value: "))
# b=int(input("Enter the terminating value: "))
#
# while a<=b:
# print(a)
# a+=1
# print('out of while loop')

# table
# a=2
# while a<=20:
# print(a)
# a+=2
# print('table end')


# infinite loop
# a=1
# while a<5:
# print(a)
# print("this will print infinite times")
# print('to stop this, press ctrl+c')

#

# while loop with else

# a= 5
# while a<=10:
# print(a)
# a+=1
# else:
# print(a)
# else will be printed in the last when the while condition gets wrong
# but if while condition is wrong a first time then else block will be executed at first.

# a=10
# while a>11: --> here the conidtion is false then the else block will be executed
# print(a)
# a+=1
# else:
# print("this esle is executing")

# infinite loop
# while(True):
# print('hello friends chai p lo \t')

# handling infinte while loop

# i = int(input("Enter the initial value: "))
# j = int(input("Enter the final value: "))
#
# while(True):
# print(i)
# i += 1
# if(i <= j):
# break
# print("we are out of while\n")

# nested while loop

# i = int(input("Enter the first value: "))
# j = int(input("Enter the second value: "))
# end = int(input("Enter the final value: "))
# 
# while (i <= end):
    # print("outer loop i value", i)
    # i += 1
    # while(j <= end):
        # print("inner loop j value", j)
        # j += 1
    # print("we are again in inner loop")
# # print("we are out of loops becuase the value of i and j is",i,j,"and it fails the condition becuase the ending was", end)
# 