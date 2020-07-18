# getting input in dict
# make empty dict
# ask size


a = {}
size = int(input("Enter the size of the dict: "))

for data in range(size):
    key = input("Enter the key : ")
    val = input("Enter the  value : ")
    a.update({key: val})

print("The updated dict is")
print(a)

print()
print("printing all keys")
all_keys = a.keys()
print(all_keys)
print()
print("printing all values")
all_val = a.values()
print(all_val)
