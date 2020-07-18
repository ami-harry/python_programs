# passing and returning set from function


'''
# without passing the set returnig a set from function
def show():
    a = {342, 56, 23, 57, 'harry'}
    print("Set inside function")
    print(a)
    print(id(a))
    print()
    return a


rec_set = show()
print("The recieved  set is ")
print(rec_set)
print(id(rec_set))
print('printing elements using for loop')
for i in rec_set:
    print(i)
print()



'''

