# index method
# this method returns position number of first occerence of given element in the list.. if doesn't find the element it will show valueError
# it returns a value which we can store and print. this will be the index no
a = []  # empty list
size = int(input("Enter the size of the list : "))
# taking input
data = 0
for data in range(size):
    print("Enter the element for index no", data, end='')
    a.append(input(": "))
print("The original list is ", a)

ind_ele = input("Enter the element to find its index no: ")
pos = a.index(ind_ele)  # index will be reutrned in pos
print("The index no of the element", ind_ele, " is ", pos)

# if any element exits twice in the list it will return the index of first occerence
# if any value didn't found. it will return valueError
