# asking the user to enter the no of elements did he want to add
# and finally printing the array elements


"""
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

a = int(input("how many elements do you want to add"))
if (a <= len(arr)):
    for new in range(a):
        arr.insert(int(input("Enter the index no: ")),
                   int(input("Enter the value: ")))

else:
    print("Enter a valid range: ")
    exit(0)

for data in range(len(arr)):
    print("element at index no",data,"is",arr[data])

print("out of loop")

"""


import array as hk
arr = hk.array('i', [])

size_of_array = int(input("Enter the size of the array :"))

print()
print("Entering array elements ")
for element in range(size_of_array):
    arr.append(int(input("Enter the array values :")))

print()
print("printing array elements using while loop")
w = 0
while (w < len(arr)):
    print("value at index no ", w, "is", arr[w])
    w += 1

print()
print("printing array elements using for loop")
for eleme in range(len(arr)):
    print("value at index no ", eleme, "is", arr[eleme])

print()
print()

new_ele = int(input("Enter how many elements you want to add:"))
n = 0
if (n <= new_ele):
    for ele in range(new_ele):
        arr.insert(int(input("Enter the index no: ")),
                   int(input("Enter the element: ")))
    n += 1

else:
    print("Invalid range \n range must be less than ",
          len(arr), "you have intered", n)
    exit(0)

print()
print("Printing updated array using while loop")
ind = 0
while (ind in range(len(arr))):
    print("value at index no ", ind, "is", arr[ind])
    ind += 1

# print()
# print("Printing updated array using for loop")
# for eleme in range(len(arr)):
    # print("value at index no ", eleme, "is", arr[eleme])
# 
# print("out of loop")
