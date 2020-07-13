
# formal and actual arguments
# formal arguments(parameters)
# -->The arguments which are passes during definition of functions

# actual arguments
# -->the arguments which are passed when function is called is actual arguments

# types of actual arguments
# a. positional arguments
# b. keyword arguments
# c. default arguments
# d. variable length arguments
# e. keyword variable length arguments


# a. positional arguments
# these arguments are passed to the function in correct positional order. the number of arguments and their positions in the function should be equal to the number of position of the arguments in the function call.

# def pow(x, y):
# z = x**y
# print(z)
#
#
# pow(10, 2) # it take the value respectively as passed in formal arguments.x=10 and y=2
# pow(2, 10) #here x=10 and y=10
# if we pass more or less arguments then it will through an error


# keyword arguments
# these arguments are passes to the function with name-value pair so keywprd arguments identify the formal arguments by their names.
# the keyword argument's name and formal arguments nname must match
# no need to maintain positions but no of arguments must be same

# def show(name, age):
# print(name, age)
#
#
# show(name="Harry", age=20)
# show(age=21, name="Harry")
# here no need to maintain the order of arguments but yes the name of arguments must be same
# no of arguments cann't be less or more

# default arguments
# sometimes we mention default value to the formal arguments in the function definition and we may not required to provide actual argument, in this case default arguments will be used by the formal arguments
# if we didn't provide actual arguments forb the formal arguments explicitly while calling the function then fromal argument will use default value on the other hand if we provide actual argument then it will use provided value.
#
# def show(name, age=21):
# print(name, age)
#
#
# show(name="Harry")
# here it takes age from formal arguments and name from actual arguments
#
#
# def show(name="Harry", age=21):
# print(name, age)
#
#
# show()
# here we have provided nothing in actual it has used all formal values
#
#
# def show(name, age=21):
# print(name, age)
#
#
# show(name="Harry", age=20)
# here the age will be replace  by the actual paramater value
# actual parameter has more precidence then formal parameter


# variable lenth argument
# this argument can accept any number of values. the variable length argument written with * symbol
# it accepts values in tuple


# def add(*num):
#     sum = num[0]+num[1]+num[2]+num[3]
#     print(sum)


# add(5, 23, 45, 234, 33)
# here the values will be accessed using index no
# no matter if the no of actual arguments are more then the index wrriten. it will run
# but if no of actual arguments are less than index wrriten, it will through an eror as tuple index out of range


# def add(x, *num):
#     sum = x+ num[0]+num[1]+num[2]+num[3]
#     print(sum)


# add(115, 23, 45, 234, 33, 45, 23)
# here the first value will be go to x and then after all values will be allocated for the num


# keyword variable length :
# this argument can accept any no of values provided in the form of key-value pair
# the keyword variable length is written with ** symbol
# it stores all the values in the dictionary in the form of key-value pair

# def add(**num):
#     z = num['a']+num['b']+num['c']
#     print(z)


# add(a=20, b=34, c=14)
# here the values are kept using key value pair and it is searching for key the output is coming


def add(x, **num):
    z = x + num['a']+num['b']+num['c']
    print(z)


add(23, a=10, b=34, c=14)
# here no need to write that x=23 , it will automatically search for it
# but for key value pair we have to mention like that
