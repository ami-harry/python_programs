# discard and remove
# we can delete elements using remove() and discard() methods
# remove() gives an error if the element is not found in the set
# discard() gives no error if the element is not found in the set

a = set()
a = {34, 23, 56, 34, 'harry', 23, 23, 'hk'}

print("The original set is")
print(a)
print(id(a))
print(type(a))
print()
# deleting the elements using remove method
a.remove('hk')
# a.remove('ramu') #ramu is not in the set it will  give an error
print("after update the set is ")
print(a)
print(id(a))
print(type(a))


# if we give any element that is not is set the remove method will give error but discard method will not give any error
print()
print("before deletion the set was ")
print(a)
print()
a.discard('harry')
a.discard('ramu')  # ramu is not in the set it will not give any error
print("The updated set is")
print(a)
print(type(a))
print(id(a))
