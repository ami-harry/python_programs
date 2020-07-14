# function decorator
# decorator function is a function that accepts a function as parameter and returns a function
# a decorator takes the result of a function, modifies the result and returns it
# in decorator, functions are taken as the argument into another funciton and then called inside the wrapper function
# we use @function_name to specify a decorator to be applied on another function


# def outer(num):
# def inner():
# print("Inner function: before calling the function")
# num()
# print("Inner function: after calling the function")
# return inner
#
#
# def modifi_fun():
# print("This function is to be modified")
# print("This will done through another function" )
#

# ret_res = outer(modifi_fun) #passing the function as the argument. this funcion is taking a function as a paramter and return a funtion. this is called decorator function.
#  so call the returned function we have to use ()

# ret_res()


# using @funcion_name method


# def outer(num):
# def inner():
# print("Inner function: before calling the function")
# num()
# print("Inner function: after calling the function")
# return inner
#
# @outer # by using this we can make the fuction as decorator and simply call the function
# def modifi_fun():
# print("This function is to be modified")
# print("This will done through another function" )
#
# modifi_fun()
#


# using single function

# def outer(modifi_fun):
# def inner():
# print("Inner function: before calling the function")
# modifi_fun()
# print("Inner function: after calling the function")
# return inner
# here we are using a single functio as a paramter,arument and as a returned value and it is working

# def modifi_fun():
#     print("This function is to be modified")
#     print("This will done through another function")

# modifi_fun=outer(modifi_fun)
# modifi_fun()


###################################################################################################
# using decor function
'''
def decor(fun):
    def inner():
        a = fun()
        add = a+10
        return add
    return inner


def num():
    return 20


# storing the returned result into a function variable
ret_res = decor(num)
print(ret_res())
'''


'''
# using @fun_name
def decor(fun):
    def inner():
        a = fun()
        add = a+10
        return add
    return inner


@decor
def num():
    return 20


print(num())
'''

'''
# using a single function name for everything
def decor(fun):
    def inner():
        a = fun()
        add = a+10
        return add
    return inner


def fun():
    return 20


fun = decor(fun)
print(fun())
'''

'''

# using decor as per user input

def decor(fun):
    def inner():
        a = int(input("Enter a value: "))
        b = fun()
        # here the value returned by fun() will be collected into b
        add = b+a
        return 'the sum is', add
    return inner


def num():
    a = int(input("Enter a value: "))
    return a


ret_res = decor(num)
print(ret_res())


'''


# concating user name as per his input using decor function

'''
def name(first_name):
    def inp():
        b = input("Enter you first name: ")
        name = b+first_name()
        print("Your name is ", end='')
        return name
    return inp


def usr_name():
    fir_name = input("Enter your last name :")
    return fir_name


ret_name = name(usr_name)
print(ret_name())

'''

'''
# using @fun_name method


def name(first_name):
    def inp():
        b = input("Enter you first name: ")
        name = b+first_name()
        print("Your name is ", end='')
        return name
    return inp

@name
def usr_name():
    fir_name = input("Enter your last name :")
    return fir_name

print(usr_name())
'''


# using single function name for actual and formal argument and storing the reurned function variable then printing the output by calling the same variable. //doing everything using a single function


def name(usr_name):
    def inp():
        b = input("Enter you first name: ")
        name = b+usr_name()
        print("Your name is ", end='')
        return name
    return inp


def usr_name():
    fir_name = input("Enter your last name :")
    return fir_name


usr_name = name(usr_name)
print(usr_name())
