# reduce function
# it returns a single value as int
# this function is used to reduce a sequence of elememts to a single value by ptoessing the elements according to a format supplied . it returns a single value. it is a part of functools module, so we have to import that modude firstz
# syntax
# from functools import reduce/*
# reduce(funcname,sqeuence)

from functools import *
a = [34, 23, 56, 23, 67, 2]
# this function will return the sum of this list, that will be a single value


print('the original list is ', a)
print()
res = reduce(lambda x, y: x+y, a)
print(res)


print()
res1 = reduce(lambda x, y: x-y, a)
print(res1)
print()

res2 = reduce(lambda x, y: x*y, a)
print(res2)
print()

res3 = reduce(lambda x, y: x/y, a)
print(res3)
