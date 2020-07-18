# slicing on nested tuples
tup = ((0, 'hii', 'hello', 35, 2),
       (1, 'hii', 'ok', 35, 2),
       (2, 45, 43, 35, 2),
       (3, 34, 'hello', 'thik hai', 2),
       (4, 'hii', 43, 35, 'achha'),
       (5, 223, 'hello', 35, 2),
       (6, 134, 12, 35, 2),
       (7, 8765, 'hello', 35, 'hi'),
       (8, 'hii', 43, 35, 2),
       (9, 123, 12, 35, 2),
       (10, 987, 'hello', 35, 'hello'),
       (11, 235, 'bye', 35, 2))

print("The original tuple is:")
print(tup)
print()

print("Printing all nested tuples using for loop with index no")
for ele in range(len(tup)):
    print('at index no ', ele, ' the element is ', tup[ele])
print()

print("First four nested tuples")
a = tup[:4]
print(a)
print()

print("last four nested tuples")
b = tup[-4:]
print()

print("from 0th pos to 6th pos")
c = tup[0:7]
print(c)

print("From 0 to last with step size 2")
d = tup[::2]
print(d)
print()

print("last 5 tuples with [-5-(-3)]=2 towards right")
e = tup[-5:-3]
print(e)

print("nested 2nd pos, then its 0th pos")
# slicing a nested tuple will also give a nested tuple
# so we can extract its elements using its own index
f = tup[2:3]
print("second pos nested tuple is")
print(f)
print()
print("printing 0th pos of this nested tuple")
# g=f[0] or
g = tup[2:3][0]
print(g)
print()

print("last 4 nested tupele and its 1pos")
h = tup[-5:]
print("last 4 nested tuples is")
print(h)
# extracting 1 pos from last 4 nested tuples
i = tup[-5:][1]
print("1st pos of last 4 tuples is")
print(i)
print()
print("extracing 1st pos elements using for loop from last 4 nested tuples")
for ele in i:
    print(ele)
print()

print("Slice 2nd tuple then extract elements")
j = a[2:3]
print("the send nested tuple is")
print(j)
print()
print("Extracing elements of 2nd pos tuple")
k = a[2:3:][0]
# k=j[0]
for data in k:
    print(data)
print()
