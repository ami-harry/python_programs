# repetition of list
# * opearator is used to repeat the elements of the list
#  it will make a new list after multiplying by the no of reperation of the list element and will be strored in  a list varible and we can print it

my_list = []  # empty list
size = int(input("Enter the size of the list : "))
# taking input
data = 0
for data in range(size):
    print("Enter the element for index no", data, end='')
    my_list.append(input(": "))
print("The original list is ", my_list)

no_of_rep = int(
    input("Enter how many times you want to repeat the elements of the list:"))
rep_ele = my_list*no_of_rep
print("the new list is :\n", rep_ele)
print()
