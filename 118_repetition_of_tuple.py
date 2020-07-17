# repetition of tuple
# using * we can print any no of times of the tuple
# syntax --> new_tuple=tuple*no of times to be multiplied

a = ["harry", 1, 'hk']
# printing this 10 times
print("The original tuple was ", a)
no_of_times = int(
    input("Enter how many times you want to repeat this tuple: "))
b = a*no_of_times
print()
print()
print("Before repetition the length of this tuple is ", len(a))
print("after repetition the length of this tuple is ", len(b))
print()
print()
print("the new tuple is:")
print(b)
print()
print("id of old tuple was", id(a))
print("id of new tuple is", id(b))
