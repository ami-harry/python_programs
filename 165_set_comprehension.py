# set comprehension
# it represents creation of new set from an iterable object that satisfy a givem condition
# syntax--> new_set{exp for item in iterable_object if_statement}

# there can be zero of more if statement
# there can be one or more for statement

# without set comprehension
set1 = {34, 2, 46, 23, 76, 23, 8, 34, 5, 23}
# making an empty set and copying this into the new one
set1_cpy = set()  # empty set
# adding the data of set1 into set1_copy by adding 10 to each element
for i in set1:
    set1_cpy.add(i+10)

print("The original set1 is\n", set1)
print()
print("The copied set1_cpy was\n", set1_cpy)
print()
# the output will be in any order becuase set doesn't follow the index order


# doing the same with set comprehension
set2 = {3, 54, 2, 4, 23, 7, 23, 67, 233, 8, 34, 5, 23}
set2_cpy = {i+10 for i in set2}
print("The original set2 is\n", set2)
print()
print("The copied set2_cpy was\n", set2_cpy)
# duplicate element will not be printed


# without set comprehension generating the set data using range function
set3 = set()  # this is an empty set and we will fill data in it using for loop and range function

for i in range(20):
    set3.add(i)
print()
print("The set data by for loop and range function is ")
print(set3)
print()

# doing the same..generating the data in a set using set comprehension and using range function
set4 = {i for i in range(20)}
print("The set data by set comprehension and range function is ")
print(set4)
print()


# multiple if statement wihtot set comprehension
# generating data in set as per multiple conditions

set5 = set()
for i in range(100):
    if(i % 2 == 0):
        if(i % 3 == 0):
            set5.add(i)


print("the set data is with multiple conditions: ")
print(set5)
print()
# generating data with multiple if statement using set comrehension
set5_sc = {i for i in range(100) if(i % 2 == 0) if(i % 3 == 0)}
print("the set data is with multiple conditions by set comprehension: ")
print(set5_sc)
print()
print()
# generating odd data by normal method
set_odd = set()
for i in range(50):
    if(i % 2 != 0):
        set_odd.add(i)

# this willl give all odd nos becuase we have passed the even conditions
print("odd data by general method")
print(set_odd)
print()

# generating odd data by set comprehension
set_odd_sc = {i for i in range(50) if(i % 2 != 0)}
print("Odd data by set comprehension")
print(set_odd_sc)

print()
# generating odd data by normal method
set_even = set()
for i in range(50):
    if(i % 2 == 0):
        set_even.add(i)
    else:
        pass
print("even data by general method")
print(set_even)
print()
print()


# generating even data by set comprehension
set_even_sc = {i for i in range(50) if(i % 2 == 0)}
print("even data by set comprehension")
print(set_even_sc)
