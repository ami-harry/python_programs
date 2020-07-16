# passing to to function as actual parameter and return nothing
# we will make a list and will pass it at function calling time and will pass the list as its actual parameter

# creating function
def show(lst_rec):
    print("The list recieved in the fuction is ", lst_rec)
    print("type is ", type(lst_rec))
    # accessing the elements of the list using for loop with index
    for data in range(len(lst_rec)):
        print("At index no ", data, " the element is ", lst_rec[data])
    print("out of function")
    print()


pas_lst = ["this", 34.4, "is", 34, "passing",
           "to", 34, "the", "function"]  # this is a list
print("The original list outside the function is: ", pas_lst)
print()
show(pas_lst)  # passing the list at function call time
