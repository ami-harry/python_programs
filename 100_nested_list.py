# nested loop
# a list within a list is called nested list or nesting of loop


# this is nested list , a list [34,23] within the list
a = [10, 20, 30, 34, [34, 23], 32, 23]
print("The nested  list is :", a)

print("The value a[2] is ", a[2])
print("The value at a[4][0] is ", a[4][0])
print("The value at a[4][1] is ", a[4][1])
print("The value at a[5] is ", a[5])

# modifying values
a[3] = 500
a[4][1] = "harry"
print("the updated  list a is", a)
# we have a nother method to make nested loop

a1 = [3, 45, 34.34, 45.23]
a2 = [45, "harry", "hk"]
# this is a list having two list its element and those two list have their own element and their own index no
print()
a3 = [34, 123, 23, a1, 45, 23, a2, 56.34]
print("The original nested list a3 is: ", a3)
print()
print("The  elemets of list a1 which is in the original list a3 as an element ", a1)
print()
print("The  elemets of list a2 which is in the original list a3 as an element ", a2)
print()

# accessing the list using index no
print("The value a3[2] is ", a3[2])
print("The value at a3[3][0] is ", a3[3][0])
print("The value at a3[3][1] is ", a3[3][1])
print("The value at a3[3][2] is ", a3[3][2])
print("The value at a3[3][3] is ", a3[3][3])
print("The value at a3[6][0] is ", a3[6][0])
print("The value at a3[6][1] is ", a3[6][1])
print("The value at a3[6][2] is ", a3[6][2])
print("The value at a3[4[] is ", a3[4])
print("The value at a3[7] is ", a3[7])

print("The value at a[5] is ", a3[5])

# now modifying list
a3[3][0] = "hii"
a3[6][2] = "Hello"
a3[2] = "hmmmm"
print("the updated list a3 is is ", a3)


# there is anoter way to create list
# this list has the elements as list and list elements has also their list
ori_list = [[34, 23, 35], [34, 34, 23], [35, 546, 34]]
print("the original list is ", ori_list)

# accessing the element using index
print("Element at ori_list[0][0] is", ori_list[0][0])
print("Element at ori_list[0][2] is", ori_list[0][2])
print("Element at ori_list[1][0] is", ori_list[1][0])
print("Element at ori_list[1][2] is", ori_list[1][2])
print("Element at ori_list[2][0] is", ori_list[2][0])
print("Element at ori_list[2][1] is", ori_list[2][1])

# modifying the list elements
ori_list[0][0] = "harry"
ori_list[1][0] = "hariom"
ori_list[2][1] = "ram"
print()
print("The updated list is ", ori_list)
