# taking input from the user in list
# copying the data into anoter list with updated value
# asking the increment size for the every element

# and printing the list with increase data

list_usr_inp = []  # empty list
size = int(input("Enter the size of the list: "))

for data in range(size):
    user_inp = int(input("Enter your data in integer only: "))
    list_usr_inp.append(user_inp)

print("The list original list is :")
print(list_usr_inp)
# copying this data into anther list with adding 5 in each elements
added_list = []  # empty list
incr = int(input("Enter how much you want to add in each element: "))

# putting the data with update value in the new list from the user input list
for data in list_usr_inp:
    added_list.append(data+incr)

print()
print("the new list with added", incr, " to each element")
print(added_list)
