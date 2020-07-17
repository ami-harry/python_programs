# tuples()
# tuples contains a group of elements can be same or different data types
# tuples are immutable
# it is similar to list but tuples are read onlu which means we cann't modify its element
# tuples are used to store data which should not be modified
# it occupies less memory compare to list
# tuples are represented using parenthese()
# we can create a tuple without () also but it must have more than 1 element


# creating empty tuple
a = ()  # this is an empty tuple
print(type(a))

print()
# creating tuple
a1 = (20)  # this not a tuples, it is an integer, if a tuples an only one element it must have a comma after the integer
print(a1)
print(type(a1))
print()

a2 = (20,)
print(a2)
print(type(a2))
print()

a3 = (4, 45, 23.45, 'hariom', '4')
print(a3)
print(type(a3))
print()

a4 = 'hii', 45, 23.45, 'hariom', '4'  # tuples without parenthese
print(a4)
print(type(a4))
print()

# accessing tuples
a5 = 34, 'harry', 2, 5, 23, 'hii', 3.35, 'hello'
print('original a5 is ', a5)
print()
print('value at a5[2] is ', a5[2])
print()
print('value at a5[5] is ', a5[5])
print()
print('value at a5[7] is ', a5[7])
print()
print('value at a5[6] is ', a5[6])
print()


