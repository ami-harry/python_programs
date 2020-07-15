# append method in list
# this method is used to add an element at the end of the existing list
# syntax --> list_name.append(new_element)

a = [34, 34, 56.34, "Harry", "Ishrat", 34.23]
print("The list before append", a)
print("Printing the data before append using index")

for data in range(len(a)):
    print("At index no ", data, " the value is ", a[data])

print()

a.append("Manisha")
a.append("Mishti")
print("The list after append", a)
print("Printing the data after append using index")
data = 0
for data in range(len(a)):
    print("At index no ", data, " the value is ", a[data])
