# making a array as per user input inside the function and reutrning the array using index

import array as hk


def my_fun():
    arr = hk.array('i', [])  # empty array
    # asking the size of the array
    size_of_array = int(input("Enter the size of the array: "))
    for data in range(size_of_array):
        print("Enter the value for index no ", data,end='')
        arr.append(int(input(" ")))

    print()
    print("The original array inside the function is :", arr)
    print("printing the array using index and value using while loop: ")
    print()
    data = 0
    # printing the data after finding the length of the array
    while data in range(len(arr)):
        print("at index no ", data, " the value is ", arr[data])
        data += 1
    print()
    return arr


# callling the function it will return an array so we have to keep it in a variable.
a = my_fun()
print("Array returned by the function is ", a)
print(type(a))
print()
print("Printing the data using index and value by for loop")
print()
data = 0
for data in range(len(a)):
    print("at index no ", data, " the value is ", a[data])
