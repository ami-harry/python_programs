
a5 = 34, 'harry', 2, 5, 23, 'hii', 3.35, 'hello'
print('the original a5 is ', a5)
# using for loop
print("using for loop with index")
for i in range(len(a5)):
    print('at index', i, " value is ", a5[i])

print()
i = 0
print("using for loop without index")
for i in a5:
    print(i)
