# make a list
# take input
# print the list
# ask how many elements user wants to add
# take input again
# print the list

a = []  # empty list
size = int(input("Enter the size of the list:"))
print("Enter ", size, " elements for the list ")

# taking input

data = 0
while data in range(size):
    print("Enter the data for index no ", data, end='')
    a.append(input(": "))
    data += 1


print()
print("the list is ", a)
print()

opt = int(input("Enter 1 to add more elements and any number:"))

if(opt == 1):
    noe = int(input("Enter how many elements you want to add :"))
    print("Enter ", noe, " new elements for the list")
    # adding elements
    data = 0
    for data in range(noe):
        print("Enter ", data, " element :", end='')
        a.append(input(": "))
    # printing the updated list
    print("the updated list is ", a)
elif(opt == 0):
    print("Thanks for using this program :")
    print("the original list was ", a)
    print()
    exit(0)
else:
    print("You have entered ", opt)
    print("Thanks for using this program :")
    print("the original list was ", a)
    print("You have to enter only 1 to add and number to close the program")
    exit(0)
