
a = {'harry', 'java', 'hk', 'ramu', 'android'}
b = {'speaker', 'sound', 'java', 'hari', 'harry', 'shanu', 'rahul'}

print("the original set a is :", a)
print("the original set b is :", b)
print()
# intersection method
intersection_met = a.intersection(b)
print(intersection_met)
print()
# this will give the common elements between the both sets


# union
union_met = a.union(b)
print(union_met)
print()
# it will print all the elements and repeated elements will be printed only once

# difference
difference_meth_in_a = a.difference(b)
print(difference_meth_in_a)
# this will return those elements which are in set a but not in set b
print()
difference_meth_in_b = b.difference(a)
print(difference_meth_in_b)
# this will return those elements which are in set b but not in set a


# issubset
a1 = {'harry', 'hk', 54}
b1 = {'harry', 'hk', 54, 'hmm'}
issubset_method_of_a1 = a1.issubset(b1)
# this will return true becuase set a is in b but all the elements of b is not in set a so in second case it will return False
print(issubset_method_of_a1)
issubset_method_of_b1 = b1.issubset(a1)
# this will return False, becuase b has 5 elements and  a has 4 elements are
print(issubset_method_of_b1)

# this method returns True or False
# this statement means a.issubset(b) means all the elements of set a is in set b or not
# this statement means b.issubset(a) means all the elements of set b is in set a or not


print()
c1 = {'harry', 'hk', 54}
d1 = {'harry', 'hk', 54, 45, 23, 23}
is_superset_d1 = d1.issuperset(c1)
print(is_superset_d1)
# this is_superset_c1 = d1.issuperset(c1) -> statement says that is d1 has all the elements of set c1. if it is then it is True meand d1 is the father for c1
#
is_superset_c1 = c1.issuperset(d1)
print(is_superset_c1)
# this will return false becuase c1 id not a superset of for d1
print()