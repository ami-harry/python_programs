# passing a tuple to a function

def show(t):
    print("The recieved tuple in the function is:")
    print(t)
    print(type(t))
    print('Extracing elements of the tuple inside the function')
    for i in t:
        print(i)
    print()
    print("printing the elements using index inside the function")
    for i in range(len(t)):
        print("at index ", i, " the value is ", t[i])
    print()


tup = ('harry', 54, 2, 45, 45, 'bye')
show(tup)
# calling the function and passing the tuple as its actual parameter
