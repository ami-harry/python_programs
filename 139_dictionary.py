# dictionary{}

# a dictionary represents a group of elements in the form of key value pair
# dictionaries in python are an unordered collection
# dictionaries are immutable so we modify its ite without changing their identity
# dictionaries are represented using curly brackets {}

# creating an empty dictionary
# a={} this is an empty dictionary

# creating dictionary
# a dictionary is created in the form of key-value pair where keys can not be repeated and of immutable type but values can be repeated and can be duplicated
# keys are case sensitive


# std = {101: 'harry', 102: 'hk', 103: 'harry', 'ravi': 200, 'hariom': 102}
# here key name can be anything,, an integer, string and all but must be unnique except list and dictionary
# here value name can be anything,, an integer, string and all
# in the dictionary ravi and hariom are as keys and harry hk are as values


# key rules
# while writing keys we must follow the following rules
# key should be unique
# if we mention same key again, the old key will be overwritten, we will loss the old data
# we can not use list or dictionary as key name


# accessing dictionary
# we can access the value of a dictionary by referring to its key name inside square brackets
# a[key_name]
std = {101: 'harry', 102: 'hk', 103: 'harry', 'ravi': 200, 'hariom': 102}
print("the original dictionary is ")
print(std)
print(id(std))
print(type(std))
print()

# accessing the dictionary using key names
print(std[101])
print(std[102])
print(std[103])
print(std['ravi'])
print(std['hariom'])


