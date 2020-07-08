# slicing on arrays:
# slicing on array can be used to retrieve a picece of the array that contains a group of elements slicing is useful to retrieve a range of elements.

# syntax--> vari=array_name[start:stop:stepsize]

import array as hk
arr = hk.array('i', [])
size_of_array = int(input("Enter the size of the array: "))

for i in range(size_of_array):
    arr.append(int(input("Enter the array elements: ")))

print()
print("The original array")
i = 0
for i in range(len(arr)):
    print("The element at index no", i, "=", arr[i])

print()
print("Array after slicing a=arr[1:5] it means from",
      "1 to 4 becuse stop value works to n-1 so 5-1 is 4")

start_val = int(input("Enter the starting slice value: "))
end_val = int(input("Enter the stopping/ending slice value: "))
step_val = int(input("Enter the step count slice value: "))


# for i in arr[-4:]:

for k in arr[start_val:end_val:step_val]:
    print(k)
print("out of loop")

"""
a = arr[start_val:end_val:step_val]

i = 0
for i in range(len(a)):
    print("The element at index no", i, "=", a[i])
print("out of loop")

"""
# slicing using for loop


# slicing can be done in many ways
# we can slice the values using for loop
# arr[0:7]-->this means from 0 to 6 it will print
# arr[:7]-->this means from 0 to 6 it will print
# arr[0:]-->this means from 0 to end of the array
# arr[-4:-2]-->this means from last of the array it will filter 4 elements and then filter 2 elemnts and between those filtered elements the value will be printed
# arr[-4:]--> this means that it will return last four element of the array
# arr[2:9:2]--> this means that it will start from 2 to 9 and will skip every 2nd no
# 2,4,6,8th index value will be printed
#
