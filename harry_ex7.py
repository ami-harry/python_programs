# making a array as per user input inside the function and reutrning the array using index


# import array as hk

'''
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




'''

# array ke under ke function bnega and wo data uska user dega size ke accoriding fir uska original data ek baar function me print krna hai fir uska data printi jo return krega wo print krna hai


import array as hk


def my_fun():
    my_array = hk.array('i', [])  # empty array
    size_of_array = int(input("Enter the size of the array: "))
    # taking the input for the array
    data = 0
    for data in range(size_of_array):
        print("Enter the element for index no ", data, end='')
        my_array.append(int(input(": ")))

    print()
    print("The data of the array inside the function is ")
    data = 0
    while data in range(len(my_array)):
        print("The element at index no ", data, " is ", my_array[data])
        data += 1
    print()
    return my_array


a = my_fun()  # calling function and storing the array in the variable a
print("the array returned by the function is ", a)
print(type(a))
print("Data as per index and value:")
data = 0
while data in range(len(a)):
    print("The element at index no ", data, " is ", a[data])
    data += 1


# using numpy


# def my_fun():


# using numpy.
# creating an empty 1D array inside the function and inserting value as per user inuput and returning the updated array and printing the array ouside the function with index and value
'''

def my_fun():
    # asking the size for 1D zeros array
    size_of_array = int(input("Enter the size of the array: "))
    my_array = hk.zeros(size_of_array, dtype=int)  # empty 1D zeros array
    print("The original array is :", my_array)
    data = 0
    while data in range(len(my_array)):  # taking the input
        print("Enter the data for index no ", data, end='')
        usr_inp = int(input(": "))
        my_array[data] = usr_inp  # storing the input
        data += 1
    print()
    print("The array after data input is :", my_array)
    print()
    return my_array


a = my_fun()  # storing the array after returning from the array
print("The array returned by the function is ", a)
print(type(a))
data = 0
for data in range(len(a)):
    print("The value at index no ", data, " is ", a[data])
print('')
'''
