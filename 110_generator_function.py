# generator fucntion()
# generator function is used to generator a squence of numbers/values. we use yield statement to return the value from the function

# yield stattemt
# this statement  returns the value from a generator  function into to generator object
# syntax-->yield a

# next()
# this function is used to retieve data element by element from the generator object.
# syntax-->next(generator_object)
'''

def show(a, b):
    yield a
    yield b  # this statement is returning the value we will store it into a object of generator class
# this is generator function


# res = show = (10, 20) # this will give return type as tuple
# here res is the generator object
# we will extract data form this object using next

# we can change this return type to list and all
# print()
# lst_res = list(res)
# print(lst_res)
# print(type(lst_res))
# print()
# print("Again checking the type of function")
# print(res)
# print(type(res))
# meanwhile the type is changed only for once..


res = show(10, 20)
print()
print(res)
print(type(res))
# accessing the element using next function
print('first element ',end='')
print(next(res))
print('second element ',end='')
print(next(res))


'''

# creating generator function and returning range of functions


def range_of_num(a, b):
    while a <= b:
        yield a
        a += 1
# this is a generator function


res_of_num = range_of_num(1, 20)
# here we have given a range from 1 to 20 it go to function and will check condition and retrun the values
print(res_of_num)
print(type(res_of_num))
# printing the elements using next statement
print('printing directly using next function')
print(next(res_of_num))  # 1
print()
print('printing directly using next function')
print(next(res_of_num))  # 2
print()
print('printing directly using next function')
print(next(res_of_num))  # 3
print()
a = next(res_of_num)  # here we are storing and printing the value.
print('value stored in a')
print(a)  # 4
print()
print('value stored in b')
b = next(res_of_num)  # here we are storing and printing the value.
print(b)  # 5
print()
# this will give continious number from the res_of_num .
# if we use loop then it will escape those elements which already have been printed
print('values using loop')
for rest_ele in res_of_num:
    print(rest_ele)
