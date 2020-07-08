# accessing array using for loop


import array as hk

arr = hk.array('i', [10, 20, 30, 40, 50])

print("printing all array elements using for loop")
for i in range(len(arr)):
    print("value at index no ", i, "is", arr[i])
print("out of loop")
print()
print()
print()
print("printing all array elements using for loop")
j = 0
while j in range(len(arr)):
    print("value at index no ", j, "is", arr[j])
    j += 1
print("out of loop")

print()
print()
print("printing elements with another method of while loop")
len_of_array = len(arr)
k = 0
while (k < len_of_array):
    print("value at index no ", k, "is", arr[k])
    k += 1

print("out of loop")

print()
print()

print("printing elements with if condition")
l = 0
if (l < len_of_array):
    print("value at index no ", l, "is", arr[l])
    l += 1
    print("value at index no ", l, "is", arr[l])
    l += 1
    print("value at index no ", l, "is", arr[l])
    l += 1
    print("value at index no ", l, "is", arr[l])
    l += 1
    print("value at index no ", l, "is", arr[l])
    l += 1


print("out of loop")
