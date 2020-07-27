# this is main project file
# here we will import of module files


'''
# this is import module_name type

import cal


cal.name()
sub = cal.sub(10, 5)
print("the addidion is ", cal.add(5, 10))
print("the subtraction is ", sub)
mul = cal.mul
print("The miltiplication is ", mul(5, 10))
d = cal.div
div = d(10, 5)
print("the division  is ", div)
print("the square is:", cal.square(5))
print("the cube is:", cal.cube(5))

'''

'''

# this is import module_name  as alias_name type

import cal as c

c.name()  # it will print the function name()
add = c.add(5, 10)
print("The addition is ", add)
print("The substraction is ", c.sub(10, 5))

'''

'''

# this is from module_name import var_name.., fun_name1, fun_name 2 as alias_name type


from cal import name as nm, add as sum, sub as diff, square

nm() # this will print the name method

s=sum(10,20) # this will add the numbers
print("the sum is ",s)
print("the substraction is ",diff(10,5))
print("The square is ",square(10))
'''

'''

# this is from module_name import *
#  (*) means all

from cal import *

print(var)
name()
print("the addition is ",add(23,23))
print("the substraction is ",sub(123,23))
s=square(5)
print("The square is",s)
'''