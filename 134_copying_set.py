# copying set into another set

# copy() method will copy  all the elements of  a set into another set

# for the new set a new address will be allocated


a = set()

a = {34, 45, 23, 46, 'harry'}
print("The set a is ")
print(a)
print(id(a))
print(type(a))
print()
# copying set into b:
b=a.copy()
print("The copied set is")
print(b)
print(id(b))
print(type(b))
print()

# b has another address and a has its own