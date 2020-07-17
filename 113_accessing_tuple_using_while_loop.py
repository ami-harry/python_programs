a5 = 34, 'harry', 2, 5, 23, 'hii', 3.35, 'hello'
print('the original a5 is ', a5)
# using while loop
print()
print("using for while loop without index")
i = 0
while i in range(len(a5)):
    print(a5[i])
    i += 1
print()
print("using while loop with index")
i = 0
while i in range(len(a5)):
    print('at index', i, " value is ", a5[i])
    i += 1
