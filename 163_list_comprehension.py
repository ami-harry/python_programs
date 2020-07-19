# comprehension
# comphrension contains very compact code usually a single statement that perform a task
# list comprehension
# set comprehension
# dict comprehension

# list comprehension
# it represents creation of new list from an iterable object that satisfy a given condition
# syntax--> new_list=[expression for item in iterable_object if_statement]

# there can be zero or more if statement
# there can be one or more for loops


# list1=[i+1 for i in range(20)] #list comprehension without if statement
# list1=[i+1 for i in range(20) if(i%2==0) ]  #list comprehension with one if statement
# list1=[i+1 for i in range(20) if(i%2==0) if(i%3==0) ]  #list comprehension with multiple if statement


# lets copy a list elements to another using normal for loop
# here we have manually the data in the list
# and we will copy that data into another list

'''
li_1 = [2, 46, 23, 46, 23, 67, 23]
print("the original list is")
print(li_1)
print()
li_2 = []  # in this list we will copy the data from first list using for loop

for i in li_1:
    li_2.append(i+5)

print("The updated list 2 is with increment 5 in each element of list 1")
print(li_2)
print()

# generating the data  using range function
list_emp = []  # this is empty list and we will put data into it using range function
print("Before updatation the list_emp is ")
print(list_emp)
for i in range(20):
    list_emp.append(i)
print("the updated data in the list_emp is ")
print(list_emp)
print()


# modifying the data of list_emp into anoter list with user_inp size
incr = int(input("Enter by how many you want to multiply with  "))
list_incr_by_usr = []

for i in list_emp:
    list_incr_by_usr.append(i*incr)

print("The list after update with *5 in each element")
print(list_incr_by_usr)

'''

# now doing the same task using list comprehension
'''
li_1 = [2, 46, 23, 46, 23, 67, 23]
print("the original data in list1 is:")
print(li_1)
print()
# copying the data using list comprehension in other list  with some updatation
lis_2 = [i+5 for i in li_1]
print("The list2 after +5 in each element of list 1")
print(lis_2)

print()
lis_3 = [i*5 for i in li_1]
print("The list3 after *5 in each element of list 1")
print(lis_3)
'''

# generating data using range in list comprehension
list1 = [i for i in range(50)]
print(list1)
print()
# using single if statement in list comprehension
list2 = [i for i in range(50) if i % 5 == 0]
print(list2)
print()
# using multiple if statement in list comprehension (nested if)
list3 = [i for i in range(51) if(i % 5 == 0) if (i % 10 == 0)]
print(list3)
print()

# # using if-else statement in list comprehension
list5 = [i for i in range(500) if(i % 5 == 0) if (i %
                                                  10 == 0) if (i % 15 == 0)]
print(list5)


# using if-else statement in list comprehension
list4 = [i if (i % 2 == 0) else "odd" for i in range(20)]
print(list4)
print()
