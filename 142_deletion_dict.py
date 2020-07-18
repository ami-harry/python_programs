# deletion
# we can delete an item or whole dict using del statement
std = {101: 'shalini', 102: 'shalu', 103: 'keshav'}
print("before deletion the dict is")
print(std)
print(id(std))
print()
del std[102]  # deleting the key 102
print('after deletion')
print(std)
print(id(std))

print("Deleting the whole dict")
del std
print(std) #here we will get an error that std is not defined becuase it is delete, it is no more
