#  if we give unnceccary space then --> IndentationError: unexpected indent error will occur.

# operators.
# operators are symbols that performs some operations
#
# 1. arithimatic operator
# 2. bitwise operator
# 3. assignment operator
# 4. relational/ comparison operator
# 5. membership operator
# 6. logical operator
# 7. identity operator


# 1. arithimatic operator
# used to perform basic arithimetic operations
# +,-,*,/,%, **(exponent),//(int division/floor division(round me answer dega))
# a=5+5
# print('5+5=',a)
# a=5-2
# print('5-2=',a)
# a=5*3
# print('5*3=',a)
# a=4/2
# print('4/2=',a)
# a=5%2
# print('5%2=',a)
# a=5**2
# print('5**2=',a)
# a=5//2
# print('5//2=',a)
# a=-5//2
# print('-5//2=',a)

# Relational/ comparison operator
# reltional operators are used to compare the values of operands or expression to produce a logical value as True or False

# a=5<2
# print('5<2', a)
# a=5>2
# print('5>2',a)
# a=5<=2
# print('5<=2',a)
# a=5>=2
# print('5>=2',a)
# a=5!=2
# print('5!=2',a)
# a=5==2
# print('5==2',a)
#

# Logical operators
# it is used to connect more relational operation to form a complex compasion called logical expression. a value obtained by evaluating a logcal expression is always logical i.e., True or False

# local and
# logical or
# local not

# logical and
# True  True    True
# True  False   False
# False True    False
# False false   False
# True  Exp     Exp
# False Exp     False
# #### True and Exp1 and Exp2 and Exp3....ExpN -->output will be always Expn
# #### False and Exp1 and Exp2 and Exp3....ExpN -->output will be always False
#
# a=10
# b=5
# c=4
# e1=100
# e2=200
# e3=400
# d=(a>b and b>c)
# e=(a>b and b>a)
# f=(a<b and a>c)
# g=(a<b and a<c)
# h=(a>b and c)
# i=(a>b and c and e1 and e2 and e3)
# j=(a<b and c)
# k=(a<b and c and e1 and e2 and e3)
#
#
# print("a=",a,"b=",b,"c=",c)
# print(a,">",b,"and",b,">",c,"is",d)
# print(a,">",b,"and",b,">",a,"is",e)
# print(a,"<",b,"and",a,">",c,"is",f)
# print(a,"<",b,"and",a,"<",c,"is",g)
# print(a,">",b,"and",c,"is",h)
# # print("here c is an expression and the last expression will be the output if the first condition is True")
# print(a,">",b,"and",c,"and",e1,"and",e2,"and",e3,"is",i)
#
# # print("here c is an expression and the last expression but the output will always be False becuase the first condition is False")
# print(a,"<",b,"and",c,"is",j)
# print(a,"<",b,"and",c,"and",e1,"and",e2,"and",e3,"is",k)
#
#

# logical or
# True  True    True
# True  False   True
# False True    True
# False False   False
# True  exp     True
# False exp     exp1
# #### True and exp1 and exp2 and exp3....expn -->output will be always True
# #### False and exp1 and exp2 and exp3....expn -->output will be always exp1

# b=5
# c=4
# a=10
# e1=100
# e2=200
# e3=400
# d=(a>b or b>c)
# e=(a>b or b>a)
# f=(a<b or a>c)
# g=(a<b or a<c)
# h=(a>b or c)
# i=(a>b or c or e1 or e2 or e3)
# j=(a<b or c)
# k=(a<b or c or e1 or e2 or e3)
#
# print(a,">",b,"or",b,">",c,"is",d)
# print(a,">",b,"or",b,">",a,"is",e)
# print(a,"<",b,"or",a,">",c,"is",f)
# print(a,"<",b,"or",a,"<",c,"is",g)
# print(a,">",b,"or",c,"is",h)
# # print("here c is an expression and the last expression will be the output if the first condition is True")
# print(a,">",b,"or",c,"or",e1,"or",e2,"or",e3,"is",i)
#
# # print("here c is an expression and the last expression but the output will always be Exp1 becuase the first condition is False")
# print(a,"<",b,"or",c,"is",j)
# print(a,"<",b,"or",c,"or",e1,"or",e2,"or",e3,"is",k)
#

# logical not
# True-->False
# False-->True
#
# a=5
# b=10
# c=(a>b)
# d=(a<b)
# print("originally condition was ",a,">",b,"is",c)
# print("but by using not operator it reversed the original output as",not(c))
# print(" originally condition was",a,"<",b,"is",d)
# print("but by using not operator it reversed the original output as",not(d))


# Assignment operators
# asignment operators are used to perform arithmetic operations while assigning a value to variable
# =, +=, -=, *=, /=, %=, **=, //=

# a = 10
# b = 20
# y = a+b
# print(a, "+", b, "=", y)
# m = 15
# m=m+10
# m+=10
# m-=10
# m*=10
# m/=10
# m%=10
# m**=2
# m//=10
# print(m)


# Bitwise operators
# bitwise operators are used to perform operations at binary digit level.
# these operations are not commonly used and are only used in special operarions where optimzed use of storage is required

# & --> Bitwise AND
# | --> Bitwise OR
# ^ --> Bitwise exclusive OR or Bitwise XOR
# ~ --> Bitwise invesion(one's compliment)
# << --> Shifts the bits to left
# >> --> Shifts the bits to right
#

# Bitwise AND (&)
# True 1 & True 1 --> True 1
# True 1 & False 0 --> False 0
# False 0 & True 1 --> False 0
# False 0 and False 0 --> False 0

# a=10
# b=15
# print(a,"&",b,"is",a&b)
# c=(a&b)
# print(c)

# Bitwise OR(|)
# True 1 | True 1 --> True1
# True1 | False 0 --> True1
# False 0 | True1 --> True1
# False 0 | False 0 --> False 0

# a=10
# b=15
# print(a,"|",b, "is",a|b)

# Bitwise XOR
# True 1 ^ True 1 --> False 0
# True 1 ^ False 0 --> True 1
# False 0 ^ True 1 --> True 1
# False 0 ^ False 0 --> False 0

# a=10
# b=15
# print(a,"^",b,"is", a^b)


# Bitwise NOT(~)
# it will change 0 to 1 and 1 to 0 and output value will be -ve (signed)
# True 1 --> False 0
# False 0 --> True 1

# a=10
# print(a,"~ is",~a)
# print("it will give -ve value as output")


# Bitwise Left shift <<
# after shifting the bits the empty boxes contain 0 bydefault

# a=10
# print(a,"<< left shift by 2 is",a<<2)

# Bitwise Right shift
# after shifting the bits the empty boxes contain 0 bydefault

# a=10
# print(a,">> right shift by 2 is",a>>2)


# Membership Operator
# it is useful to test fot membership in a sqeuenced such as list, tuple and dictionaries
# two type of membership operators.
# 1. in
# 2. not in

# in
# it searches by character by character if found then will return True else False

# har="hello to everyone"
# print('to' in har)
#
# har="hello tooo everyone"
# print('to' in har) #here it found to in too so condition matched..it is found in sqeuenced so returned true
# print('top' in har)

# sh=[10, 20,"hk", "harry", 490]
# print('harry' in sh)
# print('h' in sh) #here in list it searches for only one value means alone h and not found so it returned false

# 2. not in
# this o/p works in reverse manner of in o/p
# if element is not found it will return true and is found it will say false.


# har="hello to everyone"
# print('to' not in har)
# 
# har="hello tooo everyone"
# # print('to' not in har) #here it found to in too so condition matched..it is found in sqeuenced so returned true
# print('top' not in har)

# sh=[10, 20,"hk", "harry", 490]
# print('harry' not in sh)
# print('h' not in sh) #here in list it searches for only one value means alone h and not found so it returned false
#


# Identity Operators
# the identity operators compare the memory location of two objects. hence it is possible to know wether two objets are same or not
# two types of identity operators
# a. is
# b. is not

# a. is
# this operator is used to compare wether two objets are same or not.
# it returns True if the memory location is same else it returns False.

# a=10
# b=10
# print(a is b)
# print("here address is allocated for 10 means for value(object). a and b are just tagged with 10 to a?ccess 10 but a & b have not their own address. so both are tagged with same address so the cond?ition is true")

# a=10
# b='10'
# print(a is b)
# # print("here a is tagged with an integer type value and b is tagged with a string . so addrees of int and string is different so a and b are accessing different address so it will return false")

# b. is not
# this operator works in reverse of is operator
# it returns True if the memory locations are not same and returns False when the meory locations are same

# a=10
# b=10
# print(a is not b)
# # print("actually a and b both are tagged with same address of 10 ,but nature of is not condition will give output as false")

# a=10
# b='10'
# print(a is not b)
# print("here address is not same but ouput will be true becuse of is not operator")
# # print("here a is tagged with an integer type value and b is tagged with a string . so addrees of int and string is different so a and b are accessing different address")
