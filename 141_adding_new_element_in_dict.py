# adding new element in the dictionary
# we can add an item to dictionary just by mentioning  a new key-value pair into an existing dictionary
# if we mention a key which is already in the dictionary then the old value will be replaced by the new value
# the new item may be added at any place in the dictionary becuase dictionary is an unordered collection

std = {101: 'shalini', 102: 'shalu', 103: 'keshav'}
print("The original dict is")
print(std)
print(id(std))

# updating the value
std[104] = "keshav ji"  # here a new key value pair will be added
std[102] = "shalini ji"  # here at old value will be replace with the new one
print()
print("After adding the value the dict is")
print(std)
print(id(std))
# before and after , the id is same means no new object is created. the new pair was added to the old object id
