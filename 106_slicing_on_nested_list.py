# slicing on nested list

a = [[0, "hariom", 34, 23],
     [1, 2, "harry", 3],
     [2, "hi", 5, 6],
     [3, 8, 9, "hmmm"],
     [4, 11, 12, "hello"],
     [5, "haha",  14, 15],
     [6, 17, "aww", 19],
     [7, 21, "haaa", 22],
     [8, 24, "no", 25]]

# this is nested loop
print("The original list is : ", a)
print()

print("Elements from position 2  to 6th position: ")
sl1 = a[2:7]
print(sl1)
print()

print("print 0 to 5th position ")
sl2 = a[:6]
print(sl2)
print()

print("Printing all elements with 2 step")
sl3 = a[::2]
print(sl3)
print()


print("last 4 elements")
sl4 = a[-4:]
print(sl4)
print()

print("last 4 elements with 2 step")
sl5 = a[-7::2]
print(sl5)
print()

print("last 5 list with [-5-(-3)=2 list ")
sl6 = a[-5:-3]
print(sl6)
print()


print("slice  only nested 2nd position, and after that  oth position of nested 2nd position list")
sl7 = a[2:3]
# it will give 2nd postion  after that we will extract data of the second position list
print(sl7)
# yha pe jo value aaya wo ek list ka list hai
# slicing this second position list


# printing oth postion of this nested 2nd position list
sl7_0 = a[2:3][0]
# yha pe us list ka 0th postion ka element extract kr rahe hai or ye v ek list hai
# isme sirf ek list hai isiliye sirf 0th position ka ka niklega
# 0th pos ke elements ko loop se extract kr skte hai

# printing data of 0th position of 2nd nested loop
sl7_0_data = a[2:3][0][0]
# ye mujhe 2nd nested list ke 0th posistion vale list ke 0th position ka value dega
print("at 0th position", sl7_0_data)
print()

# printing all elemets at this index
for ele in range(len(sl7_0)):
    print("at position", ele, "the vaue is ", sl7_0[ele])
print()

# same we are taking last 4 list and form those four we will take its 2nd postion and will print the data of 2nd position list
print("The last 4 lists are")
sl_l4 = a[-4:]
print(sl_l4)
print()
print("element at 1th pos of this last 4 list:")
sl_l4_0ele = a[-4:][0]
print(sl_l4_0ele)
print()

print("element at 2th pos of this last 4 list:")
sl_l4_1ele = a[-4:][1]
print(sl_l4_1ele)
print()
print("Extracting data of this 2nd position from those 4 nested list:")
print("at 0th position of the 2nd position list from last 4 nested list")
sl_l4_1ele_0th_pos = a[-4:][1][0]
print(sl_l4_1ele_0th_pos)
print()
print("all the data of this position using loop")
data = 0
while data in range(len(sl_l4_1ele)):
    print("At index ", data, " the element is ", sl_l4_1ele[data])
    data += 1
print()
# print("printing all the data of this 2nd position of form those 4 nested list ")
