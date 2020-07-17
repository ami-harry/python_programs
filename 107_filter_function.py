# higer order function
# when we pass a function inside function


# filter()
# the filter function is used to filter out the element of an iterable (sequence) depending on a funcion that test each element in the sequence to be True or not. it returns those element of squence for which function is True
# syntax--> filter(function_name, iterable object)
# it returns a value so we can store it and will print the value
# by default it return a filter object we can manually change its return  value in different form

# function_name=it is name of function which tests each element in the sequence and return True or not. if Function is NONE, it return onlyn True value

# iterable --> this may be either a sequence , list, string, tuple a container which supports iteratin or an iterator


a = [23, 46, 23, 67, 23, 78, 344, 86]


def high(n):
    if n >= 40:
        return True


res = filter(high, a)
print('res', res)
print(type(res))
print()

res1 = list(filter(high, a))
print('res1', res1)
print(type(res1))
print()

res2 = filter((lambda x: (x >= 40)), a)
print('res2', res2)
print(type(res2))
for i in res2:
    print(i)
print()

res3 = list(filter((lambda x: (x >= 60)), a))
print('res3')
for i in res3:
    print(i)
print(type(res3))
print()


res4 = list(filter(None, a))
print('res4', res4)
print(type(res4))
print()

b = [True, False, True, False, True, False, True, False, True, False, ]
res5 = list(filter(None, b))
print('res5', res5)
print(type(res5))
print()
