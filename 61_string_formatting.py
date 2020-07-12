# string formatting
# c-style formatting
# format() method
# f-string/ formatted string literals

# c-style formatting
#  % operator / modulo operator/ interpolation operator.
# this operator is  used for formatting strings. it interprets the left arguments much like as printf() style format. string to be applied to the right argument and returns thye string from this formatting operation.
# syntax.
# print("format placeholder"%(data))
# format placeholder-> %[flags][width][.placeholder]type
#  % marks the start of the specifier
# flags --> it affects the result of some conversin type
# width --> minimum field width
# precision -> given as . followed by the precision
# type --> conversion type
# data --> it can be literal, variable, expression etc.

# ex-
# print("my name is %s and my age is %d" % ("hariom", 20))
# here %s and %d are place holders/ specifiers
# % modulo operator


# here we have to maintain the placeholder order
# after % in the (data), data is here

# if we didn't want to maintain order
#  syntax
# print("format placegolder"%{'key':'value'})
# we will use key value pair
# it is called key mapping

#
# print("My name is %(name)s and my age is %(age)d" %
#   {'age': 20, 'name': "Harry"})
# print("hey this is %(py)s and we are reading video no %(no)d ok" %
#   {'no': 93, 'py': 'python tutorial'})
# here nm and ag is key value pair and it will lool into dictionary for the pair


# conversion type               meaning
# 'd'                   signed integer decimal
# 'i'                   signed integer decimal
# 'o'                   signed octal value
# 'u'                   obsolute type. it is identifier to 'd'
# 'x'                   signed hexadecimal (lowercase)
# 'X'                   signed hexadecimal (uppercase)
# 'e'                   floating point expression format (lowercase)
# 'E'                   floating point expression format (uppercasecase)
# 'f'                   floating point decimal format
# 'F'                   floating point decimal format


# flags         meaning
#  #            used with O, X, or x specifiers the value is preceded with O,Oo,OO,Ox or Ox respectively
#  O            the conversion will be zero padded for numeric for numeric values
#  -            this converted value is left adjusted (overrided the 'O' conversion if both are given)
# <space>       (a space) , a blank should be left before a positive number(or empty string) prodced by a signed conversion

#  +            a sign character ('+' or -'-) will be precede the conversion (overrides a <space> flag).


# print("%d" % 100)
# print("%d %d" % (100, 200))
# print("%f" % 100.123)
# print("%f" % 100.123456)
# print("%f" % 100.123456789)
# print("%s" % "Harry")
# print("%s %s" % ("Hii", "Harry"))
# print("%s %d" % ("Harry", 100))
# print("%d %s" % (20, "Harry"))
# print("%d %s" % ("harry", 20)) --> it will give type error if we didn't follow the order
#
# now we will use key mapping for avoiding order precision
# print(" %(string)s %(num)d" % {'num': 20, 'string': 'Harry'})
# # print("this value is printed using %(st1)s and %(st2)s pair and we can also print %(num)s using this %(va)s pair" %
#   {'num': "digits and floating point numbers ", 'st2': "Value", 'va': "key and value ", 'st1': "key"})
#
# a="%s" % (100)
# print(a)
# print(type(a))
# print("%d"%234)
# print("% d" % 234) #here it will print a only one space.
# # print("%                               d           before d it will print only one space                 hi this is only one space" % 234) #here it will print a only one space.
# print("%+d" % 234)


# 
# print("%d" % 4567)
# print("%8d" % 4567)
# print("%08d" % 4567)
# print("%f" % 4567.533)
# print("%.3f" % 4567.556733)
# print("%.2f" % 4567.54533)
# print("%9.2f" % 4567.52333)
# print("%09.2f" % 4567.34533)
# print("%9.2f" % 45673434543434.5344333)
# 