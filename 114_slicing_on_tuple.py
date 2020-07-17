# slicing on tuple
# slicing on tuple can be used to retireve a piece of tuple that contains a group of elements. slicing is useful to retieve a range of elements
# syntax--> new_tuple_name=tuple_name[start:stop:step_size]

a = (23, 65, 23, 'harry', 46, 'hello', 54, 'hii', 'hhmm', 'achha')

print('the original tuple is', a)
print()

print('from 1st position to 4th position')
sl1 = a[1:5]
print(sl1)
print()

print("from 0th position to 6th position")
sl2 = a[:7]
print(sl2)
print()

print("0th position to last possition")
sl3 = a[::]
print(sl3)
print()

print("last 4 elements")
sl4 = a[-4:]
print(sl4)
print()

print("From 0th position to 6th position with stepsize 2")
sl5 = a[:7:2]
print(sl5)
print()

print("last 5 elements with [-5-(-3)]=2 elements towards right")
sl6 = a[-5:-3]
print(sl6)
print()
