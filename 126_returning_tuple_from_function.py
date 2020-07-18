# passing and returning tuple from a function

'''
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
    return t  # here we are returning the tuple


tup = ('harry', 54, 2, 45, 45, 'bye')
rec = show(tup)  # here are storing the recieved tuple inside the rec
print("The returned  tuple from function is  :")
print(rec)
print(type(rec))
'''


# returning a tuple without passing a tuple

def show():
    tup = (34, 23, 56, 'hii', 'by')
    print('tuple inside the funcion is ')
    print(tup)
    return tup


ret_tup = show()  # calling the function and string the returned tuple inside the ret_tup
print()
print("The returned tuple from the function is")
print(type(ret_tup))
print()
print("printing elements using index")
for data in range(len(ret_tup)):
    print("At index no ", data, " the value is ", ret_tup[data])

print()
