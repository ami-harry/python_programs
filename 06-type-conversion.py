# coverting one data type into anoter 
#  implicit and explicit

# implicit
# in this conversion, python automatically converts one data type into anoter data type

# a=10 # int
# b=3 #int
# c=a/b
# print(c)
# print(type(c)) # int no converted into float

# h="harry"
# k=" hariom"
# l=(h+k)
# print(l)
# print(type(l))




# a=10
# b='10'
# c=a+b
# print(c)
# we can add an integer and a string
# it can be possible in explicit type conversion
# print(type(c))


# explicit type conversion
# int the cast/explicit type conversion , programmer converts one data type into anoter data type
# int(n)
# float(n)
# complex(n)
# complex(x,y) -->where x is real  part and y is imaginary part
# str(n)
# list(n)
# tuple(n)
# bin(n)
# oct(n)
# hex(n)

# integer to float
# a=5
# b=2
# c=a/b
# print("value in float",c)
# print(type(c))
# print("value in integer",int(c))
# print(type(a),"+", type(b),"=",type(c))
# 
# changing the value from float into int is not a good idea. becuase we are loosing our decimal data here. so be careful while type conversion of the numbers.

# float to integer
# a=10.5
# b=int(a)
# print(type(a),"and", type(b))
# print(a,b)
# 

# integer to complex
# a=10
# b=complex(a)
# print(a,", now the value in complex form is ",b)
# print(type(a),"changes into", type(b))

# a=10
# b=complex(5,a)
# print(type(a), type(b))
# print(a,"the value into complex form",b)
# print(type(a),"changes into", type(b))
# here 5 is real part and 10j is imginary 


# integer into string
# a=10
# b=str(a)
# print(type(a), "changes into ", type(b))
# print(a, "is now ", b)
# now the 10 is not in integer it will assume as string

# string into integer
# a="10"
# b=int(a)
# print(type(a), type(b))
# print(a,"is now",b)
# now here it changes becuase of mathematical expression
# texts cant be changed into integer. only digits can change from integer into string

# string to tuple()
# a="harry hk"
# b=tuple(a)
# print(type(a), "is now ", type(b))
# print(a, " is ",b)

# string to list[]
# a="harry hk"
# b=list(a)
# print(type(a), "is now ", type(b))
# print(a, " is ",b)

# tuple() to list[]
# a=("harry 10 hariom")
# b=list(a)
# print(type(a), "is now ", type(b))
# print(a, " is ",b)

# list[] to tuple
# a=["hariom ","hk", "ishrat"]
# b=tuple(a)
# print(type(a), "is now ", type(b))
# print(a, " is ",b)

# binary
# a=100
# b=bin(a)
# print(type(a), "is now ", type(b))
# print(a, " is ",b)

# hexadecimal
# a=100
# b=hex(a)
# print(type(a), "is now ", type(b))
# print(a, " is ",b)

# octal
# a=100
# b=oct(a)
# print(type(a), "is now ", type(b))
# print(a, " is ",b)
 