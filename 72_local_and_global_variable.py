# local and global variable


# local variable
# the variable which are decleared inside a function called as local variable. local variable scope is limited only to that function where it is created. it means that local variable value is avilable only in that function not outside of that function
#
# def add(y):
# x = 10
# print("x:", x)
# print("the sum is", x+y)
#
#
# add(20)
# print(x)  # here we will see error becuase x is a local variable and cann't be access outside the function


# global variable
# when a variable is decleared above a function , it becomes global variable. these variables are avilable to all the function which are wrritten after it. the scope of global variable is the entire program body written below it.

# a = 50  # global variable


# def show():
# x = 10  # local variable
# tryping to print global variabl inside the function, it will print.
# print("Global variable:", a)
# tryping to print local variabl inside the function, it will print.
# print("Local variable", x)


# show()
# print("Global variable:", a)
# trypng to print global variable outside the function, it will print.
# print("Local variable", x)
# trying to print local variable outside the function, it will give error


# what will happen if both global and local variable has the same name
# the function will give more priority to local variable and it will ignore the global variable
# before using the local variable inside the function we have to initialize it inside the fuction

# i = 0


# def show():
# i=i+1 #this will give error that i is unassigned
# if we do it directly it will show error
# having the same name as global variable we have to initialise here it as local variable
# i = 2  # initialising the i as local variable
# i = i+5
# print("Local variable:", i)
#
#
# show()
# print("Global variable:", i)


# global keyword
# if local and global variable has same name then the function by default refers to local variable and ignores the global variable
# it means global variable is not accessable inside the function  but possible to access outside the function
# in this situation, if we need to access global variable inside the function with same name we have to access it using  globals() keyword followed by the variable name.

'''
i = 0  # global variable


def show():
    i = 0  # local variable
    i = i+1
    print(i)


show()
print(i)

'''
'''
i = 0


def show():
    global i  # this will make access the global variable
    i = i+10  # this will modify the original global variable value
    print("Global variable", i)


show()
print("Global variable", i)
'''


# i = 0
# def show():
# i = 1 # without doing this error will occur... here we have initialize i as a local variable
# while i < 5:  # here it will show error, local variable i referenced before assigned
# print(i)
# i += i

# here we will face error
# becuase every time i will get o abd while loop will not give us desired output
# we need to declare i at only one as 0, we will use global keyword and will do the same
# show()
# print("Global variable", i)


# above program using global keyword
#
# i = 0
#
#
# def show():
# global i
# while(i < 100):
# i += 10
# print(i)
#
# at here global variable will get modified
# show()
# print("Global variable:", i)
#


# global keyword
# this function returns a table of current global variable in the form of dictionary[].
# global function is used when the both local and global variable has the same name and we want to usie both and want to print the both values
# globals keyword will not modify the original value of the global varibal
# it simply keep the global value into a variable and we perform actions on that inside the function but it will not acceft the original value of the global variable

a = 50  # global variable


def show():
    a = 10
    print("local variable:", a)
    x = globals()['a']
    print("Global variable:", x)
    # accessing the global variable using globals keyword. it is just a copy of global variable. the all modifications will done locally.
    x = 40
    print("Global variable:", x)

    # this will not affect the original value
show()
print("Global variable:", a)
