# popitem() method
# this method is used to delete the last element inserted in the dict
# it returns the removed element in the form of tuple, pairs are returned into LIFo order

std = {101: 'shalini', 102: 'shalu', 103: 'keshav'}
print("the original dict is")
print(std)
print(type(std))
print()

# poipitem method
return_item = std.popitem()
print("after popitem")
print(std)
print()
print("the returned element is")
print(return_item)

# it returns the key value pair