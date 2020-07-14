# pass/call by object reference

# in c,java and some other languages we pass the value to a function either by reference widely known as "pass by value " and "pass by reference"

# in python, either of these two concept is applicable rather the vaues are send to function  by means of object reference

# when we pass value like numbers, string, tuples or list to function , the reference of these object are passed to function.


# def var(x):
#     print(x, id(x))
#     x = 15
#     print(x, id(x))


# x = 10
# var(x)
# print(x, id(x))

# a new object is created in the memory becuase integer objects are immutable(not modifiable)

# here the variable name are same no matter a new addess will be allcated for those..becuase in python new address is allocated for the object not for the variable.


# see here the both formal and actual arguments have different names and new address will be alloacted for the integer objects

# def var(a):
#     print("The original address for a")
# # here it will be tagged with the old address becuase the value is still 10
#     print(a, id(a))
#     a = 15  # by doing this new address will be allocated for the 15
#     print("The addess after changing the value of a")
#     print(a, id(a))
#     print("only this address will be changed for new value..and others will stay same")


# x = 10
# print("The original address for x")
# print(x, id(x))
# var(x)
# print("The addess after changing the value of x")
# print(x, id(x))


# all the address will be same becuase the list objects are mutable(modifiable).
# and this is not happing becuase they have the same name
# if the list is passing to the function and appedning the value will not change the address of the list

# def val(list1):
# print(list1, id(list1))
# list1.append(10)
# print(list1, id(list1))
#
#
# list1 = [1, 2, 3, 4, 5]
# print(list1, id(list1))
# val(list1)
# print(list1, id(list1))
#


# def var(list1):
#     print(list1, id(list1))
#     print("address before appending the values")
#     list1.append(100)
#     print("address after appending the values")
#     print(list1, id(list1))


# list2 = [34, 23, 56, 23]
# print(list2, id(list2))
# var(list2)
# print(list2, id(list2))
# list objects are mutable, so no new address will be allcated for the items


# in python, values are passed to function by object reference
# if object is immutable(not modifiable) then the modified value is not avaliable outside the function
# if object is mutable(modifiable) then the modified value is avaliable outside the function

# immutable objects-->integer, float, tuple,string
# mutable objects--> list, dictionary

# immutable objects
# after changing the values it will have a new addres but the address will only valid inside the function . outside the function that address is not avaliable
# mutable
# the addess outside or inside the function is same . after appending or before appending the addess are same.


# whenn we create  a new object inside the function thenit will not avaliable outside the function

# def val(lst):
#     print("Address before creating new object of same name")
#     print(lst, id(lst))
#     lst = [12, 54, 3, 67, 34, 67]
#     # new address , this will avilable only inside the function
#     print("Address after creating new object of same name")
#     print(lst, id(lst))


# lst = [23, 34, 34]
# print("the original address  outside the function is")
# print(lst, id(lst))
# val(lst)
# # this will hold the old address of the list
# print("address outside the function after creating the object ")
# print(lst, id(lst))
