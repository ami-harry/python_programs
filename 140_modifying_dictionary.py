# modify dictionary
# we can modify the existing value of key by assigning a new value
std = {101: 'one zero one', 102: 'one zero two', 103: 'one zero four'}
print("Before modification")
print(std)
print(id(std))
print(type(std))
print()

# modifying the dictionary using its key name
std[103] = 'one zero three'
print("after modification")
print(std)
print(id(std))
print(type(std))

# after modification the address will be same
# the value of that particular key will be updated at the same id. 