# accessing set using for loop
# accessing set using index is not possible
# we can extract data without index

a = set()
a = {23, 45, 'harry', 23, 67, 34.67}
# accessing this set
print("all the elements")
print(a)
print(id(a))
print()
# using loop
for i in a:
    print(i)
print('done')
print()
