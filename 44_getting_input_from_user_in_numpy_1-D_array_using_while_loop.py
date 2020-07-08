# getting input for shape of the array in zeros function
# we will enter the size and the elemeents and that input will replace the original value of the array returned by the zeros function. values will be replaced by the index no
# accessing index we can mofidy the elements of the original array.


import numpy as shalini

size_of_array = int(input("Enter the size of the array: "))

array = shalini.zeros(size_of_array, dtype=int)
print("The original array returned by the zeros function: ", array)

print()
# using for loop
"""
for data in range(len(array)):
    data_by_user = int(input("Enter the array elements :"))
    array[data] = data_by_user
"""
# using while loop
data = 0
while data in range(len(array)):
    data_by_user = int(input("Enter the array elements :"))
    array[data] = data_by_user
    data += 1

# printing data using for loop
"""
for ele in range(len(array)):
    print("The value at index no ", ele, "  is ", array[ele])
"""

# printing data using while loop
ele = 0
while ele in range(len(array)):
    print("The value at index no ", ele, "  is ", array[ele])
    ele += 1

print("out of loop")
