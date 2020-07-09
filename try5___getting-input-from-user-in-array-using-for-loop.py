# getting input to an empty array from user using append()

import array as hk
arr = hk.array('i', [])
size = int(input("Enter the size of the array: "))

for i in range(size):
    arr.append(int(input("Enter the array elements: ")))

print()
print("printing array element with for loop ")
for data in range(len(arr)):
    print("The element at index no ", data, "is", arr[data])
print()

print("printing array element with while loop ")
j = 0
while (j < len(arr)):
    print("The element at index no ", j, "is", arr[j])
    j += 1
print("out of loop")
