# values method
# this method returns the sequence of values as an object

std = {101: 'shalini', 102: 'shalu', 103: 'keshav'}
print("the original dict is")
print(std)
print(type(std))
print()

# getting all values using values() method
all_val = std.values()
print("Values returned by method")
print(all_val)
print(type(all_val))
print()
# we will typecast it into list and will aceess using index
all_val_list = list(all_val)
print("The values in list form")
print(all_val_list)
print(type(all_val_list))
print()
print("element at index no 0 is",all_val_list[0])
print("element at index no 1 is",all_val_list[1])
print("element at index no 2 is",all_val_list[2])

