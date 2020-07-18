# adding elements in set
#


# adding 1 element
# we can add  a new element to set using add() method

a = set()  # empty set
# adding one element in this empty set
a.add('harry')
a.add(20)  # by using add() method can add only one element at a time
print(a)


# adding multiple element in set
# we can add multiple elements using update() method
# the update() method can take lists, string or tuples as its argument

b = [43, 23, 'harry']
a.update(b)
print()
print("the updated set is ")
print(a)


c = (23, 3, 'hello')
a.update(c)
print()
print("the updated set is")
print(a)
