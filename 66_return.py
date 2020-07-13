# return statement
# return statement can be used to return something from the function. in python it is possible to return one or more variables/values

# syntax
# return(variable or expression)
# return 50
# return (50)
# return x
# return (x,y)
# return (x+y)


# example
# returning z from the function
def add():
    x = 10
    y = 20
    z = x+y
    return z


# to hold the returned value from the function. we have to store it in a variable. and after string we will print the value
# sum = add()
# print(sum)


def add1():
    x = int(input("Enter the first number: "))
    y = int(input("Enter the second number: "))
    sum = x+y
    diff = x-y
    return (sum, diff)


# here 2 values are returning so we have to keep it in two different variables respectively
sum1, sub1 = add1()
print(sum1)
print(sub1)
