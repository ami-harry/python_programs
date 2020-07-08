# index()
# this method returns the position of the first occurence of given element in the array. if doesn't found then will give valueError
# if a number exists multiple time then will return the first position of that number

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
ele = int(input("Enter the element :"))
if ele in arr:
    print("The position is  ", arr.index(ele), "and the element is", ele)

else:
    print("invalid element it does't exists in array")
    exit(0)

print()
