# nested list comprehension
# in nested list comprehension we have 2 for loops
# firstly the out loop exceutes and then after the inner loop executes


lst = [[16, 20, 24, 28], [20, 25, 30, 35, 40]]
# using normal method means nested for loop

'''
l = []  # making empty list to store the result of nested for loop
l1 = []  # making empty list to store the result of nested for loop
l2 = []  # making empty list to store the result of nested for loop
for i in range(4, 6):
    for j in range(4, 8):
        l.append(i*j)
        l1.append([i*j])
        l2.append([[i*j]])


print(l)
print(l1)
print(l2)
'''

# using list comprehension

lst_comp = [(i*j) for i in range(4, 6) for j in range(4, 8)]
print(lst_comp)

'''
for i in range(4, 6):
    for j in range(4, 8): 
        list_comp.append(i*j) this will also have the same value as this list comprehension has given
'''

