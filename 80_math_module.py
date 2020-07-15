# math module
# it is  a module that contains several functions to perform mathematical operatin
# if we want to use this module we have to import it first.
# from math import *

# floor(n) --> decrease n value to the previous integer value. if n is integer then same value is returned
# ceil(n) --> raise n value to the next integer higher integer. if n is integer , then same value is returned
# fabs(n) --> returns absolute value or positive quantity of n
# factorial(n) --> returns the factoril of n
# sqrt(n) --> returns the square root of n
# pow(n,m) --> returns n value to the power of m
# sin(n) --> returns the sine value of n
# cos(n) --> returns the cosine value of n
# tan(n) --> returns the tangent value of n
# gcd(n,m) --> Returns the greatest common divisior of the integer a and b. if either  a or b is non zero then the value of the gcd (a,b) is the largest positive integer that divides both a and b, gcd(0,0) returns 0.

from math import *
print(floor(4.5))
print(ceil(4.5))
print(sqrt(49))
print(factorial(4))
print(pow(4, 2))