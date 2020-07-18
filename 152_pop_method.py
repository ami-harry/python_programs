# pop() method
# this method is used to remove the item with specified key
# it returns the returned item's value
# if key is not found then default value is printed
# if key and default value is not found the it will show keyError
# it returns something so we can strore into a variable and will print the returned value
# it returns the value of the deleted key

std = {101: 'shalini', 102: 'shalu', 103: 'keshav'}
print("the original dict is")
print(std)
print(type(std))
print()

# pop an element
popped_ele = std.pop(102)
print("after pop the dict is")
print(std)
print()
print("The popped element is", popped_ele)
print()
popped_ele1 = std.pop(109, 'key not found')
print(popped_ele1)