# setdefault() method
# this method returns the value of the specific key
# if key is not found, then it inserts the key-value in the dict


std = {101: 'shalini', 102: 'shalu', 103: 'keshav'}
print("the original dict is")
print(std)
print(type(std))
print()

# using setdefault method
# this is not avilable in the dict so it will be inserted
set_default = std.setdefault(101, 'harry')
print("After set default method")
print(std)
print("the inserted value is", set_default)
print()
# 109 key is avilable..so it will be removed
set_default1 = std.setdefault(109, 'h')
print('after key is matched in setdefault')
print(std)
print("The remove element is", set_default1)
