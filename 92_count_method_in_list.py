# count
# this method returns the no. of occerence of a specified element in the list
# it returns a value. we can store and print it.this is the no of occorence

a = []  # empty list
size = int(input("Enter the size of the list : "))
# taking input
data = 0
for data in range(size):
    print("Enter the element for index no", data, end='')
    a.append(input(": "))
print("The original list is ", a)

oc_num = input("Enter the element to check how many times it is in the list: ")
val = a.count(oc_num)
print("the element ", oc_num, " is ", val, " times in the list")
