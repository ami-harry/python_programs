import array as hk
arr = hk.array('i', [])

size_of_array = int(input("Enter the size of the array: "))

# print("appendig the values into the array")
a = 0
while (a < size_of_array):
    arr.append(int(input("Enter the array element: ")))
    a += 1

print("original array")
for num in range(len(arr)):
    print("value at index no ", num, "is", arr[num])

print()
no_of_elements = int(input("enter how many elements you want to add: "))
if (no_of_elements <= len(arr)):
    for new_ele in range(no_of_elements):
        arr.insert(int(input("Enter the index no:")),
                   int(input("Enter the element: ")))
    no_of_elements += 1
else:
    print("Invalid range or range is overflow")
    exit(0)

print()
print("printing elements usign for loop")
for element in range(len(arr)):
    print("value at index no ", element, "is", arr[element])


print()

# print("printing array elements with while loop")
# b = 0
# while (b < len(arr)):
# print("value at index no ", b, "is", arr[b])
# b += 1

print("out of loop")
