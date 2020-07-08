# nonzero() function
# this function returns an array that contains the indexes of the element of the array which are not equal to zero
# this function is used to determine the position of non zero elemets

import numpy as hk
array1=hk.array([23,45,0,23,54,45.5,0,65,0,4,76.6,0,56,23])
print(hk.nonzero(array1))
# it will return an error which have the index no of non-zero elements of the array1