# without set comprehension the data in set with conditions

set5 = set()  # empty set

#  we will put the data range value as odd and even in the set

for i in range(20):
    if(i % 2 == 0):
        set5.add(i)
    else:
        set5.add('odd')
print("The set data by for loop and range function is ")

print(set5)
print()
# using if-else in set comphresension
set5_sc = {i if i % 2 == 0 else'odd' for i in range(20)}
print(set5_sc)
# both will give same data

print()


# nested set comprehension
# values b/w 4 to 9
st = {(i, j) for j in range(4, 7) for i in range(6, 9)}
print(st)
