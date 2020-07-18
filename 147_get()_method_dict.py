# get() method
# this method returns the value of the respected key
# if key is not found then it will return the default value

# dict_name.get(key, default_mesage)

key = (1, 2, 3, 4, 5, 6, 7, 8, 9)
val = ("harry", "hariom", "hk")
obtained_dict = dict.fromkeys(key, val)
print("the dict is ")
print(obtained_dict)

print()
# searching using key using get method
print(obtained_dict.get(2, 'not found'))
print()
print(obtained_dict.get(10, 'not found'))
print()
print(obtained_dict.get(4, 'not found'))
print()
print(obtained_dict.get('hk', 'not found'))
print()
