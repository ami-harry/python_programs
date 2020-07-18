# set{} type

# a set is an unordered collection of elements much like a set in mathematics
# the order of elements is not maintained in the set, it means the element may not appear in the same order as they are entered into the set
# a set does not support duplicate/repeated entry
# set is mutable so we can modify it
# sets are unordered so we can not access it using index no.
# sets are represented by curley brackets {}

# creating a set
#  a set is created by placing all the elements (items) inside the breces {}, seperated by comma. a set doesn't accept duplicate elements
# elements can be of different type except mutable elements like set, list, dictionary.

# creating an empty set
# an empty set can be created using set() function

# a = set()
# a is an empty set
# print(type(a))
# print(id(a))
# print()

# accessing set elements:
# sets are unordered , so we cant acess its elements using index.
# a = {34, 23, 'hii', 5.45, 'hello'}
# print(a[3]) # this will give error, we cant access using index
# print(a)
# every time set will give uniue output


a = {34, 23, 56, 'harry', 32, 7, 32, 67, 34, 34, 34, 'hk', 34, 34, 34, 34, 34}
# here 34 is many times but it will print it only one times
print(a)
