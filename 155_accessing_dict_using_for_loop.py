# accesssing the dict using for loop


std = {101: 'shalini', 102: 'shalu', 103: 'keshav'}
print("the original dict is")
print(std)
print(type(std))
print()

# printing all keys using for loop
for key in std:
    print("key= ", key)

print()
# printing all values using for loop
for values in std:
    print("values= ", values)
print()
# printing keys and values both
for key_value in std:
    print("at key ", key_value, " the value is ", std[key_value])


