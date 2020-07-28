# main file
# here we will import all the modules which is written in another file

# importing class, method, function, var of cal.py file in this file

from cal import Mobile, sum, square, mul, num1, num2

a = Mobile()  # this will call the constructor, a is object for the class mobile
print()
a.clsM()  # accessing the class method
print()
a.show()  # accessing instance method
print()
a.statM()  # accessing the static method
print()
print('the class variable is : ', a.mcv)
print()

sum()  # calling the sum function
print()
mul(5, 10)  # calling it with parameter
print()
square(10)
print()
print("the variable in module is :", num1)
print("the variable in module is :", num2)

mul(num1, num2)  # passing the argument as the module variable
print()
square(num2)  # passing the argument as the module variable
