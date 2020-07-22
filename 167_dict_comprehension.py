# dict comprehension


# normally using for loop
dict1 = {}  # empty dict
# we are putting the value of dict using for loop
for i in range(20):
    dict1[i] = i*2

print('values using normal for loop')
print(dict1)
print()

# using dict comprehension
dict1_dc = {i: i*2 for i in range(20)}
print('values using dict comprehension loop')
print(dict1_dc)
print()


# filling the dict using for loop with one condition
dict2 = {}
for i in range(20):
    if(i % 2 == 0):
        dict2[i] = i*2

print(dict2)

# using dict comprehension with  one condition
dict2_dc = {i: i*2 for i in range(20) if i % 2 == 0}
print()
print(dict2_dc)

# filling the dict using for loop with two conditions
dic3 = {}
for i in range(50):
    if(i % 2 == 0):
        if(i % 3 == 0):
            dic3[i] = i*2

print()
print(dic3)
print()
# using dict comprehension with two condition
dic3_dc = {i: i*2 for i in range(50) if(i % 2 == 0) if(i % 3 == 0)}
print(dic3_dc)

# if else
dic4 = {}
for i in range(1000):
    if(i % 2 == 0):
        dic4[i] = 'even'
    else:
        dic4[i] = 'odd'

print()
print(dic4)
print()
print()
# if-else using dict comprehension
dic4_dc = {i: ('even' if i % 2 == 0 else 'odd') for i in range(1000)}
print(dic4_dc)
