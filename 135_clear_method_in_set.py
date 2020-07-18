# clear all elements of the set
# clear() this method is used to remove all the elements of the set


# set_name.clear()


a = set()
a = {34, 23, 46, 23, 46, 57, 'harry'}
print("The original set is")
print(a)
print(id(a))
print(type(a))
# clearing all the elements
print()
a.clear()
print("after clearing the elements the set is" )
print(a)
print(id(a))
print(type(a))
