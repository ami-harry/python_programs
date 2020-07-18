# passing a set to function
# inside set take input and add new elements
# and return the updated set from function


# passing a function and return the same function with some updated value

def fun(st):
    print("The recieved set in function is ")
    print(st)
    print(id(st))
    print("at the time of recieved in funcion the length of set was ", len(st))
    # updating the set with user input
    print()
    size = int(input("Enter how many elements you want to add in the set: "))
    for data in range(size):
        inp_data = input("Enter your data: ")
        st.add(inp_data)
    print()
    print("the updated set after user input is ")
    print(st)
    print(id(st))
    print("after modification length of set is ", len(st))
    return st


pas_set = {'this ', 'is', 'passing', 'set', 54, 223, 57, 1}
# this is the original set which we will pas into the function at calling time as the actual paramter

print("the original set outside the function is ")
print("the length of original set is ", len(pas_set))
print(pas_set)
print(id(pas_set))
print()

# passing the set to the function while calling and storing the returned set
ret_set = fun(pas_set)
print()
print("The set recieved from the function")
print(ret_set)
print(id(ret_set))
print("the length of recieved  set from function is ", len(ret_set))
print("printing sets data using loop")
for data in ret_set:
    print(data)
print('done')
