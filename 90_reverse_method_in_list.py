# reverse method
# this method is uses to revese order of elements of the list

# syntax--> list_name.reverse()

a = []  # empty list
size = int(input("Enter the size of the list : "))
# taking input
data = 0
for data in range(size):
    print("Enter the element for index no", data, end='')
    a.append(input(": "))
print("The original list is ", a)

a.reverse()
print("List after reverse: ", a)
