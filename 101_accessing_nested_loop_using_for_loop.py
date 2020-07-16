# accessing nested loop using for loop

# creating first list
fir_lst = []  # empty list
size1 = int(input("Enter the size of the first list: "))
# taking input for first list
for data in range(size1):
    print("Eneter element for index no ", data, end='')
    fir_lst.append(input(": "))
print()

print()


# creating second list
sec_lst = []  # empty list
size2 = int(input("Enter the size of the  second list: "))
# taking input for first list
for data in range(size2):
    print("Eneter element for index no ", data, end='')
    sec_lst.append(input(": "))

print()

# creating third list
thrd_lst = []  # empty list
size3 = int(input("Enter the size of the third list: "))
# taking input for first list
for data in range(size3):
    print("Eneter element for index no ", data, end='')
    thrd_lst.append(input(": "))

print()
print("The list is ", fir_lst)
print("the length of the list is ", len(fir_lst))
print()
print("The second is ", sec_lst)
print("the length of the second is ", len(sec_lst))
print()
print("The third list is ", thrd_lst)
print("the length of the third list is ", len(thrd_lst))
print()


'''
# adding all input list in a single list
main_lst = [fir_lst, sec_lst, thrd_lst]
print("The main list is", main_lst)
print("the length of the main list is ", len(main_lst))
print()
# accessing this main list using for loop
# this list is having the elements as list only

# without index
print("The elements of the list without index")
for row in main_lst:
    for col in row:
        print(col)
    print()
print("Out of loop")


print()
# with index
print("The elements of the list with index")
for row in range(len(main_lst)):
    for col in range(len(main_lst[row])):
        print("element at row ", row, " and column  ",
              col, " is ", main_lst[row][col])
    print()
print()

'''


print()
main_lst1 = ["hey", 34, 32, 46, "harry", fir_lst, "hii",
             45, 32, sec_lst, "hmmm", "hk", 54.45, thrd_lst]
print("The original main_lst1 is ", main_lst1)
print("The length of main_lst1 is ", len(main_lst1))
# accessing this main list using for loop without index
# this list is having the elements as list and interger too only
# this will be access in other way

# accessing without index
print()
print("Printing the elements without index: ")

for row in range(len(main_lst1)):
    if type(main_lst1[row]) is list:
        if len(main_lst1[row]) > 1:
            for col in range(len(main_lst1[row])):
                print(main_lst1[row][col])
                # for index we will give row,col,main_lst1[row][col]
    else:
        print(main_lst1[row])  # for index we will give, row, main_lst_1[row]
    print()
print("Out of loop")
print()


# printing the same list using index, row and column
for row in range(len(main_lst1)):
    if type(main_lst1[row]) is list:
        if len(main_lst1[row]) > 1:
            for col in range(len(main_lst1[row])):
                print("At row ", row, " and column ", col,
                      " the element is ", main_lst1[row][col])
    else:
        print("At row ", row, " the element is ", main_lst1[row])
    print()
print("out of loop")
