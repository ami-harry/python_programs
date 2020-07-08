# extend()
# this method is used to append another array or iterable object at the end of the array
# arr1.extend(arr2)

from array import *
arr1 = array('i', [])
size_of_array1 = int(input("Enter the size of the array1: "))
for ele1 in range(size_of_array1):
    arr1.append(int(input("Enter the array elements1: ")))

arr2 = array('i', [])
size_of_array2 = int(input("Enter the size of the array2: "))
for ele in range(size_of_array2):
    arr2.append(int(input("Enter the array elements2: ")))
arr3 = array('i', [])


print()
print("printing original elements of array1")
a = 0
while (a < len(arr1)):
    print("array element at index no ", a, "is", arr1[a])
    a += 1

print()
print("printing original elements of array2")
a = 0
while (a < len(arr2)):
    print("array element at index no ", a, "is", arr2[a])
    a += 1

print()
print("Array after extending the array2 with array1")
arr1.extend(arr2)
print("printing extended elements of array1 and array2")
for data in range(len(arr1)):
    print("Element at index no ", data, "is ", arr1[data])
print()


"""
print()
print("Array after extending the array1 with array2")
arr2.extend(arr1)
print("printing extended elements of array2 and array1")
for elem in range(len(arr2)):
    print("Element at index no ", elem, "is ", arr2[elem])

print("here we are facing an error\n we are unable to extend the first array after 2nd array..it is extending but first arraay always comes first.")
"""
print("out of loop")
