# reverse()
# this method is used to reverse the order of the elements of the array
# syntax...array_name.reverse()


from array import *
arr = array('i', [])
size_of_array = int(input("Enter the size of the array: "))
for ele in range(size_of_array):
    arr.append(int(input("Enter the array elements: ")))

print()
print("printing original array")
a = 0
while (a < len(arr)):
    print("array element at index no ", a, "is", arr[a])
    a += 1

print()
print("Array after reverse: ")
arr.reverse()
for rev in range(len(arr)):
    print("Value at index no ",rev,"is", arr[rev])

print("out of loop")