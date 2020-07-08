# remove method
# this method is used to remove the first occurancec of given element from the existing array.
# if doesn't founf it was return valueError
# if a elemnt exists more then one time but the first occurence will be deleted and others will remain as same in the array

from array import *
arr = array('i', [])
size_of_array = int(input("Enter the size of the array: "))
a = 0
while (a < size_of_array):
    arr.append(int(input("Enter the array element:")))
    a += 1
print()
print("The original array is")
for ele in range(len(arr)):
    print("the element at index no ", ele, "is", arr[ele])
print()
rev_ch = int(input("Enter that element you want to delete:"))
print()

print("Array after removing the element")
rem_ele = arr.remove(rev_ch)
for data in range(len(arr)):
    print("the element at index no ", data, "is", arr[data])
print("The removed elemet was ",rem_ele)
print("it will return none becuase remove function didn't return anything")
print("out of loop")
