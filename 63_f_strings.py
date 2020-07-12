# f_string/ formatted string literals
#  a formatted string literal or f-string is a string literal that is prefixed with f or F. these strings may contain replacement fields which are expressions. delimited by curley breaces {}. while other strings literals have a constant value. formatted strings are really expressions evaluated at run time
# syntax
# f"{index/key/name:[fill][alignn][sign][#][0][width][,][.precision]type}

# a = 10
# print(f"value of a is {a}")

# name = "hariom"
# age = 21
# print(f"my name is {name} and age is {age}")

# inp_name = input("Enter your name: ")
# inp_age = input("Enter your age: ")
# print(f"your name is {inp_name} and your age is {inp_age}")


# a = 10
# b = 20
# c = f"{a+b}"
# print(c)

# dictionary
name = "harry"
print(f"{name}")
# calling functions

print(f"{name.upper()}")

# date and Time
# from datetime import datetime
# today = datetime(2020, 7, 11, 12, 20, 30)
# print(f"{today}")
# print(f"{today:%d-%b-%y}")
# print(f"{today:%d %b,%y}")
# print(f"{today:%d/%b/%y}")