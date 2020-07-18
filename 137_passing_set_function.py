# passing a set to function as argument

def show(st):
    print("The  set passed in function is ")
    print(st)
    print(type(st))
    print(id(st))
    print()
    print("printing data using loop")
    for i in st:
        print(i)


set_1 = {23, 45, 23, 'harry', 'hk'}
print('the original set outside the function is ')
print(set_1)
print(id(set_1))
print()
# calling the function and passing the set
show(set_1)
