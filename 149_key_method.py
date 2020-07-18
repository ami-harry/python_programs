# key() method
# this method returns the sequence of keys from the dictionary
# syntax--> dict_name.keys()


std = {101: 'shalini', 102: 'shalu', 103: 'keshav'}

print("the original dict is")
print(std)
print(id(std))
print()

# getting all keys using key method
all_keys = std.keys()
# it will give a sequence of keys in tuple of list form
# we will typecase it into list and will acess the items using index
print("The keys returned by items method")
print(all_keys)
print()

# typecasting the returned value
all_keys_list = list(all_keys)
print("The values in the form of list")
print(all_keys_list)
print()
print("value at index no 0",all_keys_list[0])
print("value at index no 2",all_keys_list[1])
print("value at index no 2",all_keys_list[2])
