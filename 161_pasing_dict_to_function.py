# passing dictionaty to function

def show(fd):
    print("the recieved dictitonary is")
    print(fd)
    print()
    print(type(fd))
    print()
    print(id(fd))
    print()
    print("Printing keys and values")
    for key in fd:
        print(key, '=', fd[key])


dic = {'course': 'python', 'fees': 56453, 'duration': '3months',
       'dict1_inside_first': {'course': 'python_advance', 'fees': 6476}}

show(dic)
print()
print("the original dict is")
print(dic)
print()
print(type(dic))
print()
print(id(dic))
