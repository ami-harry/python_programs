# aliasing list
# aliasing means giving a nickname for the list
# it doesn't means that copying the data
# the new nickname will also be tagged with the same memory location
# modification in anyone will affect both becuase both are tagged with same location

my_list = []  # empty list
size = int(input("Enter the size of the list : "))
# taking input
data = 0
for data in range(size):
    print("Enter the element for index no", data, end='')
    my_list.append(input(": "))
print("The original list is ", my_list)

# giving nickname for this list

ur_list = my_list
print()
print("priting my_list ", my_list)
print("priting ur_list ", ur_list)

# mofifying the list, it will affect the both

my_list[3] = "Hariom"
my_list[2] = "Ishrat"
print()
print("priting after modification in my_list ", my_list)
print("priting after modification in ur_list ", ur_list)

# priting the id of the both list
print()
print("Id of the my_list is ", id(my_list))
print("Id of the ur_list is ", id(ur_list))
