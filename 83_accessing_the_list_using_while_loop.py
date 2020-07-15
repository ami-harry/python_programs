# accessing the loop using while loop

a = [54, 23, 56, "harry", "Manisha", 34.23]

print("The original list is ", a)
print()
print("Printing the list without index using while loop")
data = 0
while data in range(len(a)):
    print(a[data])
    data += 1
print
print("Printing the list with index using while loop")
data = 0
while data in range(len(a)):
    print("At index no ", data, " value is ", a[data])
    data += 1
print("done")
