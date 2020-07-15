# accessing the list by for loop

a = [45, 34, 23, 56.34, "Harry", "manisha", "mohak", 34, 23]
print("The original list is ", a)
print()
print("printing the list without index is ")
for i in a:
    print(i)
print()
print("printing the list with index is ")
i = 0
for i in range(len(a)):
    print("At index no ", i, " value is ", a[i])
print("done")
