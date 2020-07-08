# any() and all() function

# any()
# this function returns True. if any one element of the iterable is True. if iterable is empty then it returns False

# all()
# this function returns True is all elements of the iterable are True or iterable is empty

# these functions returns only one boolean value. but comparision / relational operators return array of bool. they return boolean value for each condition in form of array

import numpy as hk
array1 = hk.array([12012, 20, 360, 240, 509])
array2 = hk.array([1340, 20, 4340, 4340, 5034])
print(any(array1 == array2))
# here only one case is matched but it will return True. becuase any one is True then the return value will be True
array3 = hk.array([12, 20, 30, 240, 509])
array4 = hk.array([1340, 230, 4340, 4340, 5034])
print(all(array3 < array4))
# here we are checking and will return the result as per condition
# here all values of array 4 is less than the values of array 3.
