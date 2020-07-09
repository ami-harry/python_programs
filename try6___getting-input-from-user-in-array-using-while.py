# taking input from user using while loop

import array as hk
arr = hk.array('i', [])

size_of_array = int(input("Enter the size of the array"))
i = 0
while (i < size_of_array):
    arr.append(int(input("Enterr the array elements:")))
    i+=1

print()
print("printing array elements using while loop")
j = 0
while (j < len(arr)):
    print("The value at index no ", j, "is", arr[j])
    j += 1
print("out of loop")
print()
print("priting the elements using for loop")

for k in range(len(arr)):
    print("The value at index no ", k, "is", arr[k])

print("out of loop")
