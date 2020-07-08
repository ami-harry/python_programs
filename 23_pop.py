# pop()
# this method is used to remove the last element of the exising array
# syntax-->array_name.pop()

"""
import array as hk
arr = hk.array('i', [])

size_of_array = int(input("Enter the size of the array: "))
i = 0
while (i < size_of_array):
    arr.append(int(input("Enter the elements: ")))
    i += 1

print()
print("the original array elements are")

for data in range(len(arr)):
    print("Element at index no ", data, "is", arr[data])

print()
print("Array elements after pop")
arr.pop()
ele = 0
# n = len(arr)
while (ele < (len(arr))):
    print("Element at index no ", ele, "is", arr[ele])
    ele += 1

print("out of loop")
"""

# pop(n)
# this method is used to remove an element specified by position number from the existing array and returns the remove element
# syntax --> array_name.pop(position_no)

"""
import array as hk
arr = hk.array('i',[])
size_of_array=int(input("Enter the array elememts: "))
a=0
while(a<size_of_array):
    arr.append(int(input("Enter the array elements: " )))
    a+=1
print()
print("Printing the original array")
for data in range(len(arr)):
    print("element at index no ",data,"is",arr[data])
print()
print("Array elements after pop")
del_item=arr.pop(2)
a=0
while(a<len(arr)):
    print("element at index no ",a,"is",arr[a])
    a+=1
print("The deleted item was ",del_item)
"""

# asking the user that from which position he wants to delete and printing the updated array


from array import *
arr = array('i', [])
size_of_array = int(input("Enter the size of the array: "))
a = 0
while(a < size_of_array):
    arr.append(int(input("Enter the elements: ")))
    a += 1
print()
print("Printing the original array")
for data in range(len(arr)):
    print("Element at index no ", data, "is", arr[data])

print()
choice = int(input("Enter the position that you want to delete: "))
if (choice >= size_of_array or choice <0):
    print("Invalid position or position overflow:")
    exit(0)
else:
    del_item = arr.pop(choice)
print()
print("printing updated array ")
a = 0
while(a < len(arr)):
    print("Element at index no ", a, "is", arr[a])
    a += 1
print("the deleted item was", del_item, "and position was", choice)
print("out of loop")
