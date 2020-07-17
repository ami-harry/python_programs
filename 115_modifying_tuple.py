# modifying tuple
# tuples are immutable so it is not possible to modify or delete its element

# to modify the tuple we take help of slicing and concatination.
# if we want to add any element in the between any slice, we have to slice first that element and  concatinate new element in the sliced area and then add it then print
# or modifycation depends upon slicing, how we slice the tuple


a = [343, 546, 5, 23, 7, 34]
b = ['harry', 'hello']
print("original a is ", a)
print()
print("original b is ", b)
print()
sl_a1 = a[:3]
print("The sliced part from 0th to 2nd position is ", sl_a1)
print()
sl_a2 = a[3:]
print("The sliced part from 3th to last position is ", sl_a2)
print()
c = (sl_a1+b+sl_a2)
print("the concatinated tuple is", c)
print()

