# anonymous or lambda function
#  a function without name is called anonymous function. it is also known as lambda function
# anonymous function are not defined using def keyword rather than they are defined using lambda keyword
# syntax
# lambda arg_list:statement/expression

# def ani(x):
#     return print(x)
# ani=lambda x:print(x)


# print("value using def function:")
# ani(5)


# def show(x, y): return x+y
# show= lambda x,y: x+y


# print("value using lambda function", show(20, 30))

# lambda function doesn't have any name
# lambda function returns a function
# lambda function can take zero or any number of arguments but contains only one expression
# in lambda function there is no need to write return statement
# it can only contain expression and cann;t include statement in its body\
# you can use all type of actual arguments

# lambda function returning two values


# def dual(x, y): return (x+y, x-y)
# dual=lambda x,y: (x+y, x-y, x*y, x/y, x**y)


# n1 = int(input("Enter the first number: "))
# n2 = int(input("Enter the second number: "))
# a, b,c,d ,e= dual(n1, n2)
# print("The sum is ", a)
# print("The diff is ", b)
# print("The mul is ", b)
# print("The division is ", b)
# print(n1,"^",n2," is ",e)


# nested lambda function
# when we write a lambda function inside another lambda function that is called nested lambda function

# def add(x=10):
#     return (lambda y: x+y)
# add=lambda x=10:(lambda y: x+y)

# a = add() #storing the lamda function retured function into a variable
# print(a) #to check that the returned value is containg a function or not
# print(a(20)) #here passing a parameter for the inner lamda function

# this is nested lambda function


# passing lambda function into another function

# n1 = int(input("Enter first value: "))
# n2 = int(input("Enter second value: "))


# def show(a):
#     print(a(n1, n2))


# show(lambda x, y: x+y)
# here while calling the function we are passing the lambda function as parameter and its arguments are taking into the main calling function


# returning lambda function from another function
# n1 = int(input("Enter a number : "))
#
#
# def add():
# y = int(input("Enter another numebr"))
# return (lambda x: (x+y)
# return (lambda x: (x+y, x-y, x*y, x/y, x**y))
#
#
# a = add()
# print(a(n1))
# a1, a2, a3, a4, a5 = a(n1)
# print("the sum is ", a1)
# print("the difference is ", a2)
# print("the multiplcation is ", a3)
# print("the division is ", a4)
# print("n1^n2 is", a5)
#


# immediately invoked function expression(IIFE)

# this function dont need to call, it automatically calls when its decleared

# old method
# def sum(x, y):
# return x+y
#
#
# print(sum(10, 20))

# we can do one thing with lambda function
(lambda x, y: print(x+y))(5, 2)
# this is the syntax


a = int(input("Enter first value: "))
b = int(input("Enter second value: "))
(lambda x, y: print("the sum is ", x+y, "\nthe diff is ",
                    x-y, "\nthe mul is ", x*y, "\nthe division is ", x/y, "\n", a, "^", b, " is ", x**y))(a, b)
