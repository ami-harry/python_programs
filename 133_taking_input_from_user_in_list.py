# geting input from user
# make an empty set
# ask size
# using loop take input and usind add method we will put input to the set

a = set()
print("the original set is")
print(a)
print(id(a))
print(type(a))
print()
size = int(input("Enter the size: "))
# taking input
for data in range(size):
    inp_data = input("Enter your elements:")
    a.add(inp_data)


print()
print("The updated set is ")
print(a)
print(id(a))
print(type(a))


print()
print("printing the data using loop")
for data in a:
    print(data)
print()






# we can also take input in list and we can update the set