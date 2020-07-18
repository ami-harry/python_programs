# copy ()
# this method use to copy all the elements of a dict to another dict
# new dict has a new address
# both

std = {101: 'shalini', 102: 'shalu', 103: 'keshav'}
print("The original dict is")
print(std)
print(id(std))

# copying this to  a new one
cop_dict = std.copy()
print()
print("the copied dict is")
print(cop_dict)
print(id(cop_dict))


# modifying the new copied dict
print()
cop_dict[103] = "this is modified"
cop_dict[107] = 'this is new added'
print("After modification the copy dictionatry is")
print(cop_dict)
print(id(cop_dict))
