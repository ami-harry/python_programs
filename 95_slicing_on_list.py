# slicing on list
# slicing on list can be used to retieve a piece of the list that contains a group of elements. slicing is useful to retieve a range of elements
# syntax >--> new_list_name=list_name[start:stop:stepsize]
# bydefault start size is 0
# stop size is upto n-1
# step size is bydefault 1 but it cann't be 0 in any case

a = []  # empty list
size = int(input("Enter the size of the list : "))
# taking input
data = 0
for data in range(size):
    print("Enter the element for index no", data, end='')
    a.append(input(": "))
print("The original list is ", a)

# performing various slicing ratios
print()
print("Elements from 0 to last position")
sl1 = a[0:]  # means from zero to last
for i in sl1:
    print(i)
print()

print("Elements from 0 to last position with stepsize 2")
sl2 = a[::2]
# sl2 = a[0::2] both are same
for i in sl2:
    print(i)
print()


print("elements from 1st postion to 5th position")
sl3 = a[1:6]
for i in sl3:
    print(i)
print()

print("elements from 3st postion to last position")
sl4 = a[3:]
for i in sl4:
    print(i)
print()

print("Last five elements using -ve index")
sl5 = a[-5:]
for i in sl5:
    print(i)
print()
print("Last 3 elements fro right using [-5-(-2)]=3 slice: ")
sl6 = a[-5:-2]
for i in sl6:
    print(i)
print()
