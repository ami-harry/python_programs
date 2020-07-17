# map function()
# map() function executes a specified function on each element of the iterable(sequence) and perhaps chaanges the element

# syntax  map(function_name, iterble_object)

# fun_name=it is name of a function which perform  an operation on all the elements of the sequence and mofidied elements are returned which can be stored in another sequence
# map function can have one or more than one iterable objects but they have same no of elements

# iterable objects must be of same type
'''
a = [45, 2, 57, 23, 7, 34, 78]


def add(n):
    return n+5


print('original elements were\n', a)
res = map(add, a)
print('after map function call', res)
print(type(res))
for i in res:
    print(i)
print()
res1 = list(map(add, a))
print('original first list is ',a)
print('after map function call', res1)
print(type(res1))

# using lambda function
# it will return all the values by increasing 10
print()
res2 = list(map(lambda x: x+10, a))
print('original first list is ',a)
print('res2', res2)
print()

# using 2 lists or iterable objects but
b = [23, 45, 23, 67, 34, 56, 34]

# making a lambda function that will takes two parameter and will return the difference between the first list and 2nd list. or substracting the values of 2nd list from first list
print('original first list is ',a)
print('original second list is list is ',b)
res3 = list(map(lambda x, y: x-y, a, b))
print('res3 is',res3 )
print(type(res3 ))
'''


str1 = ["hello", "how ", "hmm"]
str2 = [' harry', ' are you', 'good']

print('original str1 is ', str1)
print('original str2 is ', str2)
print()

res1 = list(map(lambda x: x+' achha', str1))
res2 = list(map(lambda x: x+' thik hai', str2))
res3 = list(map(lambda x, y: x+' thik hai be' + y+' chal chal be thik hai', str1, str2))



print(res1)
print()
print(res2)
print()
print(res3)
