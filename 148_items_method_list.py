# items() method
# this method returns an object as key-value pair of dictionary. the pairs are stored as tuple in the object.
# syntax --> dict_name.items()

# dictionary items() method
std = {101: 'shalini', 102: 'shalu', 103: 'keshav'}

print("original dict:")
print(std)
print()


# storing the items returned by the items() method
lst = std.items()
# this will return the values as tuple of list of tuple. ([(a,b),(c,d)]) like this for
# to extract data simply or to acess that data easily we will typecase it into list and then after we will access that list using index no
print("The data returned by the items method is ")
print(lst)
print()
print()

print("Changing the data into list")
lst_type = list(lst)
print("The data is")
print(lst_type)

# now accessing the data using index from lst_type

print()
print("the data at 0th index is", lst_type[0])
print("the data at 1th index is", lst_type[1])
print("the data at 2th index is", lst_type[2])
# extracting the data using index of its index
print()
print("at 0th index of 0th pos", lst_type[0][0])
print("at 1th index of 0th pos", lst_type[0][1])
print()
print("at 0th index of 1th pos", lst_type[1][0])
print("at 1th index of 1th pos", lst_type[2][1])
print()
print("at 0th index of 2th pos", lst_type[2][0])
print("at 1th index of 2th pos", lst_type[2][1])
print()
print()


# accessing data using for loop  for main list
print("the data of list using loop is ")
for data in lst:
    print(data)
