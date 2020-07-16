# passing and returning list from the function

def show(rec_lst):
    print("The recieved list is ", rec_lst)
    print(type(rec_lst))
    # accessing the element of list recieved using index
    for data in range(len(rec_lst)):
        print("at index no", data, " the element is ", rec_lst[data])
    print()
    return rec_lst  # returning the list


ori_lst = [45, 34, "harry", "hk"]
print("The original list is :", ori_lst)
print()
# passing the original list at calling time and stroing the reutrned list into the ret_lst
ret_lst = show(ori_lst)
print("Printing the returned list ", ret_lst)
print(type(ret_lst))
print()
for data in range(len(ret_lst)):
    print("at index no", data, " the element is ", ret_lst[data])
print()
# accessing the reutrned list using index
