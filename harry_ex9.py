# creating a list as per user input and accessing it using loops
# ex as for harry the list will be ['h','a','r','r','y']
# using range function make a list(range(start,end,stepsize))

'''
inp_str = input("Enter the string to make the list: ")
a = list(inp_str)
print()
print("Your string list is :\n", a)

print()
print("Printing the elements of the list using for loop without index")
print()
for data in a:
    print(data)
print()

print("Printing the elements of the list using while loop with index")
data = 0
while data in range(len(a)):
    col = 0
    for col in range(len(a[data])):
        print("A row ", data, " and column ", col,
              " the element is ", a[data][col])
        col += 1
    data += 1
print()
'''

inp_start = int(input("Enter the starting for range: "))
inp_end = int(input("Enter the end for  range: "))
inp_step = int(input("Enter the stepsize range: "))

b = list(range(inp_start, inp_end, inp_step))
print("Your list according to range:\n", b)
print()
print("Printing the elements without index using for loop")
for i in b:
    print(i)
print()
# print("Printing the elements without index using for loop")
# row = 0
# while row in range(len(b)):
#     print(row)
#     row += 1
print("Printing the elements with index using while loop")
row = 0
while row in range(len(b)):
    print("At index no ", row, " the value is ", b[row])
    row += 1
