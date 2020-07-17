# alising tuple
# it means giving nickname for the tuple
# it doesnt mean copying
# both can access the tuple and both have the same memory address

# if we done sicing and for this purpose a new address will be genereated becuase the sliced data will have a new memory address.

a = (34, 23, 45, 'harry', 'kh', 34, 23)
print(id(a))
b = a  # aliasing a as b
print(id(b))
print("data of a", a)
print("data of b", b)
print()

# slicing the values
a = a[2:4]
print("the sliced value is ", a)
print("the new address for sliced value is ", id(a))
print("here id of b will be same as old ", id(b))
