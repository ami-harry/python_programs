# for loop
# the for loop is useful to iterate over the elements of sqeuence such as string, list, tuple,dict.
#

# h="harry"
# for a in h:
# print(a)
# print(type(h))
# print("for loop exit for",h)
# print()
#
# b=["harry", "hariom", 50, '50', "60.354"]
# for c in b:
# print(c)
#
# print(type(b))
# print("for loop exit for",b)
# print()

# d=('harry','hk', 'ishrat', 'shalini', 50, '50', 60.60)
# for harry in d:
# print(harry)
# print(type(d))
# print("for loop exit for",d)
# print()
#
#
# dic={'harry':'boy', 'ishrat':'bou',50:'num'}
# for boy in dic:
# print(boy)
# print(type(dic))
# print("for loop exit for",dic)
# print()
#

# printing each character with their respective index
# h = 'harry hk'
# n = len(h)
# for i in range(n):
    # print(i, '=', h[i])
# print('out of loop')
# 
# here we are using range function to know the after knowing the length of the string and after that we are finding the string at that range.

# for loop with else
# the for loop is useful to iterate over the elements of sequence such as string, list , tuples etc. the else suit will be always executale irrespective of the statement in the loop are executed or not.
# else vala hmesa run krega hi

# for i in range(3):
    # print('inner loop',i)
# else:
    # print("this is else block")
# print('out of loop')


# nested for loop
# for loop inside for loop
# 
# for i in range(2):
    # print('inner loop',i)
    # for j in range(3):
        # print('1st outer loop',j)
        # for k in range(4):
            # print('2nd outer loop',k)
# print('out of loop')