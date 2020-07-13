# functions
# functions are sub programs which are used to compute a value or perform a task
# type of funtion:
# a. built-in function (ex- print(),upper(), lower(),input()..)
# b. user-defined function

# Advantage of functions
# write once and use it as manu times you need. this provides code reusability
# function facilitates ease of code maintainance
# divide large task into many small task so it will help you to debug code
# you can remove or add new features to a function anytime

# function definition
# we can define a function using def keyword followed by function name with parentheses. this is also called ass creating a function, wiritng a a function. defining a function.

# here this function has no parameter.
# def function_name():
# local_variables
# block of statments
# return(variable or expressions)

# here this function has a parameter.
# def function_name(x):
# local_variables
# block of statments
# return(variable or expressions)


# calling a function
# a fucntion runs only when we call it, funtion cann't run on its own
# syntax--> function_name() --> this is without arguments
# function_name(x) --> this is with arguments

# here the parameter x do not know which type of value they are about to recieve till the value is passed at the time of calling the function. it means that the type of data is determined only during the runtime not at the compilte time. this is dynamic typing


# a normal function without parameter
def add():
    x = 10
    y = 20
    z = x+y
    print(z)


# calling the function without arguments
# add()


# a function having parameter
def add1(x):
    y = 20
    z = x+y
    print(z)


# calling the function with arguments
# add1(10)


# function will work on user input
def ask_sum():
    x = int(input("Enter first value: "))
    y = int(input("Enter second value: "))
    z = x+y
    print(z)


# calling the function with arguments
# ask_sum()


# printing the name using function as what user inputs
def usr_name():
    name = input("Enter your name: ")
    print("Your name is ", name)


# calling the function
# usr_name()


# printing the user name using formatted string
def ur_name():
    name = input("Enter your name: ")
    print(f"your name is {name} ")
    print(f"your name is {name:.3} ")


# calling the function
ur_name()
