# pop
# this method is used to remove last element from the existing list
# syntax--> list_name.pop()
# it simply delete the element but didn't return any value

'''
a = []  # empty list
size = int(input("Enter the size of the list : "))
# taking input
data = 0
for data in range(size):
    print("Enter the element for index no", data, end='')
    a.append(input(": "))
print("The original list is ", a)

a.pop()
print("list after pop operation:", a)

'''

# pop(n)
# this method is used to remove the specific position from the list
# this function returns the remove element. we can store it and print that removed element

a = []  # empty list
size = int(input("Enter the size of the list : "))
# taking input
data = 0
for data in range(size):
    print("Enter the element for index no", data, end='')
    a.append(input(": "))
print("The original list is ", a)

pop_ele = int(input("Enter the position you want to remove: "))
rem_ele = a.pop(pop_ele)
print()
print("list after removing a element:", a)
print("the removed element was ", rem_ele)
