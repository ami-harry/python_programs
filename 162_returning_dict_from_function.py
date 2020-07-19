# returning dict without passing a dict


def show():
    dic = {'course': 'python', 'fees': 56453, 'duration': '3months',
           'dict1_inside_first': {'course': 'python_advance', 'fees': 6476}}
    print("The original dict inside the function is")
    print(dic)
    print()
    print(type(dic))
    print()
    print(id(dic))
    return dic


ret_dic = show()
print()
print("the returned  dict is")
print(ret_dic)
print()
print(type(ret_dic))
print()
print(id(ret_dic))

print("Printing keys and values")
for key in ret_dic:
    print(key, '=', ret_dic[key])


# the id will be same in function and out of the function
# while passsing and recieving the dict type and id is always same