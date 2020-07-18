# fromkeys() method
# this method is used to create a new dictionary with the specific key and value

# syntax --> dict.fromkeys(key,value)

# we can take keys and values input from the user in list, tuple and all, and after that we can give the values to the function

# here key is a list variable having 3 elements which will be used as key for our dictionary
key = (1, 2, 3)
val = "harry"
new_dic = dict.fromkeys(key, val)
print("the dict is ")
print(new_dic)
print(id(new_dic))
print()


key1 = "harry"
val1 = (1, 2, 3)
new_dic1 = dict.fromkeys(key1, val1)
print("the dict is ")
print(new_dic1)
print(id(new_dic1))
print()

# yha harry mtlb h ke liye 1,2,3 then a ke 1,2,3, then r ke 123 and all

key2 = (1, 2, 3, 4, 5)
val2 = ("harry", "shalini","keshav")
new_dic2 = dict.fromkeys(key2, val2)
print("the new dict is")
print(new_dic2)
print(id(new_dic2))
