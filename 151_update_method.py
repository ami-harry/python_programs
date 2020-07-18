# this method is used to update the dictionary with the specific key value pair
# dict_name.update(iterable)


std = {101: 'shalini', 102: 'shalu', 103: 'keshav'}
print("the original dict is")
print(std)
print(type(std))
print()

# updating the dict

std.update({'hello': 'hii'})
print("the updated dict is")
print(std)
print(type(std))
print()

# updating the dict using a dict

new_ele = {'hi': 'hello', 'help': 'ni milega',
           "achha": 'hmm', "thik hai": 'ok'}

std.update(new_ele)
print("the updated dict is")
print(std)
print(type(std))
print()

# printing all keys
all_keys = std.keys()
print("All keys are")
print(all_keys)
print()
all_val=std.values()
print("printing all values")
print(all_val)
print()
