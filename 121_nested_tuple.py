# nested tuple
# a tuple within tuple is nested tuple or nesting of tuple


# a = (10, 20, 30, ('harry', 'hk'))
# # or
# both are same
b = ('hello', 'hi')
a = (10, 20, 30, b)
# here we are seeing that element is 5 but its has a tuple as element b
# inside a nested tuple , a tuple is also considered as an element yes but for accessing its element we can do for their index value

print("nested tuple a is ", a)
print("the length of the tuple a is", len(a))
print("the length of the tuple b is", len(b))
print("the id of the tuple a is", id(a))
print("the id of the tuple b is", id(b))
print("Element at a[0] is ", a[0])
print("Element at a[1] is ", a[1])
print("Element at a[2] is ", a[2])
print("Element at a[3] is ", a[3])
print("Element at a[3][0] is ", a[3][0])
print("Element at a[3][1] is ", a[3][1])
print()
print()
a = (10, 20, 'harry')
b = ('hello', 20, 34)
c = (a, b)
print("the length of a is", len(a))
print("the length of b is", len(b))
print("the length of c is", len(c))
print("Elemets of tuple a is", a)
print("Elemets of tuple b is", b)
print("Elemets of tuple c is", c)
# accessing the tuple using index
print("Element at index no c[0]", c[0])
print("Element at index no c[1]", c[1])
print("Element at index no c[0][0]", c[0][0])
print("Element at index no c[0][1]", c[0][1])
print("Element at index no c[0][2]", c[0][2])
print("Element at index no c[1][0]", c[1][0])
print("Element at index no c[1][1]", c[1][1])
print("Element at index no c[1][2]", c[1][2])
