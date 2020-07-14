# Recusion
# a function calling itself again and again to compute a value is referred to recursive function or recursion
# if the same fuction is calling itself the limit in python is 1000,
#

# def myfun():
# print("hello Harry")
# myfun()
# myfun()
# this will print 1000 times

# i = 0


# def myfun():
#     global i  # using global variable will help to run the iterarion
#     # if we use local i then every time i will get 0 and we will face error in output
#     # so using global variable is better option
#     i += 1
#     print()
#     print("Hi harry ", i)
#     myfun()


# myfun()


# finding limits of recursion


# import sys
# print("the limit of recursion is: ")
# print(sys.getrecursionlimit())

# print("We can change the limit manually")
# sys.setrecursionlimit(500)
# print("now the limit of recursion is")
# print(sys.getrecursionlimit())


# i = 0


# def for_loop():
#     global i
#     i += 1
#     if(i <=990):
#         print("This is using for loop no", i)
#     else:
#         print("out of for loop")
        # exit(0)
#     for_loop()

# for_loop()
# print("The global value is", i)

# i = 0
# #


# def while_loop():
#     global i
#     while(i < 400):
#         print("This is using while loop no ", i)
#         i += 1
#         while_loop()
#     print("Out of while loop")
#     exit(0)


# #
# #
# while_loop()
# #
