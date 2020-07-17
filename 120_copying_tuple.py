# copying tuple
# we can copy the elements of tuple into another using slicing
# after slicing the elements are same in the new sliced then this is not copy. both will have the same address
# copying means creating a new object, it will have a new address
# so for copying purpose we will take some unique range to slice
# so the new tuple has different element and have a new id

a = (34, 56, 23, "hk", 57, 34, 76, "hary")
print("Tuple a is ", a)
print("id of Tuple a is ", id(a))
# slicing the values
b = a[0:]
# here we are copying all the elements
# this is not copy, b will also tagged with the same tuple becuase all the elements are same
# b will also have the same adress as a
print()
print("Tuple b is ", b)
print("id of Tuple b is ", id(b))


# now taking a different range to slice
# these will have a new address and will have different data
sl_1 = a[1:5]
sl_2 = a[0:3]
print("The sliced sl_1 is", sl_1)
print("The id of sliced sl_1 is", id(sl_1))
print()
print("The sliced sl_2 is", sl_2)
print("The id of sliced sl_2 is", id(sl_2))
# we can slice data from these sliced tuple also :D
# slicing data from sl1
sl_1_1 = sl_1[1:3]
print()
print("The original sl1 is", sl_1)
print("the sliced sl1_1 is ", sl_1_1)
print("The id of sl1 is ", id(sl_1))
print("The id of sl1_1 is ", id(sl_1_1))  # it has different address than sl1
