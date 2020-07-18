# clear()
# this method is used to delete all the elements of the dictionary

std = {101: 'shalini', 102: 'shalu', 103: 'keshav'}

print("Before clear the dict is")
print(std)
print(id(std))

std.clear()
print("After clear")
print(std)
print(id(std))
# the id will be same before and after clear
