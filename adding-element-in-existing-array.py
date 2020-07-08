# by using insert() we can add elements in the existing array

import array as hk
arr = hk.array('i', [])

size_of_array = int(input("enter the size of the array: "))

for data in range(size_of_array):
    arr.append(int(input("Enter the array element: ")))

print()
print("the  array elements is")
for elements in range(len(arr)):
    print("The element at index no ", elements, "is", arr[elements])

print()
print("adding new elements in the array")

arr.insert(1, 49)
arr.insert(2, 29)
arr.insert(3, 19)
arr.insert(4, 99)

print("the updated array is using for loop")

for up in range(len(arr)):
    print("the element at index no", up, "is", arr[up])
print()
print("out of loop")

print("the updated array is using while loop")
a = 0
while (a < len(arr)):
    print("the element at index no", a, "is", arr[a])
    a += 1
print("out of loop")
