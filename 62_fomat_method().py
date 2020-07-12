# format method

# this method is used to format strings. the string on which this method is called call literal text or replacement fields determined by breces{}. each field conatins the numeric index of positional argument oof the name of a keybaord argument. its field is replaced with the string value of the corresponding argument

# syntax str.format(arg)


# str = "my age is {}"
# print(str.format(20))
#
# print("my name is {}".format("harry"))

# in most of the cases the syntax is similar to the end
#  % formatting with the addition of the {} and : used insted of %

# '%d' can be transfered to {:d}
# '%05.3f' can be transfered to {:05.3f}

# print("Replacement field ".format(values))
# replacement field= {indexkey/name:[fill][align][sign][#][0][widht][,][.position]type}

# print('{}'.format(10))
# print('The value is {a}'.format(a=10))
# print('name is {a}'.format(a="harry"))

# conversion type               meaning
# d                         signed integer decimal
# 0                         signed octal value
# x                         signed hexadecimal (lowercase)
# X                         signed hexadecimal (upperrcase)
# b                         binary format
# e                         floating point expression format(lowercase)
# E                         floating point expression format(uppercase)
# f                         floating point decimal (default is 6)
# F                         same as 'f' except displays 'inf' as 'INF' and 'nan' as 'NAN'
# c                         charcater converts the integer into the corresponding unicode charcater before   printing
# g                         generalformat rounds number to p significant digits' default precision 6
# G                         same as 'g' except switches to 'E' if the number is large
# n                         same as 'd' except it uses current local string for number seperator
# s                         string (coverts any python object using str())
# %                         percentage multiplies the numbers by 100 and displays in fixed ('f') formated followed by a % sign


# alignment type                   meaning

# <                               forces the filed to be left align as written the variable space. (this is default for most of the object)

# ^                               forces the field to be centered within the avilable space
# >                               forces the field to be right aligned wiithin the avilable space.(this is default for numbers)

#  =                              forces the padding to be placed after the sign(if any) but before digits. this is used for printing fields in the form of '+000000122'. this alignment option is only valid for numeric type. it becomes the default when 'O' immediately preceds the field width.

# sign(+,-,<space>)
# -              this converted value is left adjusted (overrided the 'O' conversion if both are given)
# <space>       (a space) , a blank should be left before a positive number(or empty string) prodced by a signed conversion

#  +            a sign character ('+' or -'-) will be precede the conversion (overrides a <space> flag).


# the '#' option causes the 'altername form' t be used for the conversion. the alternate from is defined differently for the different types. this option is only valid for interger, float, octal or hexadecimal output. this option adds the prefix respective 'Ob','Oo'' or 'Ox' to the output value


# the ',' option is used to seperate the thousands value. for a local aware seprator, use the n interger presentation type instead

# the '_' option is also used instead of , for seperating the thousands value


#
# print("{}".format(10))
# print("{} {}".format(10, 20))
# print("{0}".format(10))
# print("{0} {1}".format(10, 20))
# print("{1} {0}".format(10, 20))
# print("{num1}".format(num1=10))
# print("{num1} {num2}".format(num1=10, num2=20))
# print("{num2} {num1}".format(num1=10, num2=20))
#

# integer and string

# print("hello my name is {} and my age is {}. ".format("Hariom", 20))
# print("hello my name is {1} and my age is {0}. ".format(20, "Hariom"))
# print("hello my name is {name} and my age is {age}. ".format(
# name="Hariom", age=20))


# integer
# print("***********Integer******************")
# print("{}".format(1345))
# print("{:d}".format(135435))
# print("{:0d}".format(1345))
# print("{num:d}".format(num=1245))
# print("{num:08d}".format(num=15))
# will make 8 blocks and put number from last and the remainging box will holds 0
# here 8 is width and d is type
# print("{num:+5d}".format(num=15))
#  here + is sign and will make 5 blocs and the number will be stored from right and left boxes will hold 0
# print("{num:<5d}".format(num=15))
# here < is left align. 5 boxes will make and number will be fit and remaining do holds nothing
# print("{num:*<5d}".format(num=15))
# here * is fill, the empty boxes will holds *
# print("{num:*>5d}".format(num=15))


# float
# print("********Float***********")
# print("{}".format(15.65))
# print("{:f}".format(15.65))
# print("{0:f}".format(15.65))
# print("{num:f}".format(num=15.65))
# print("{num:<5.2f}".format(num=15132.6235))
# print("{num:*<10.2f}".format(num=1523.625))
# print("{num:>10.2f}".format(num=15332.61135))
# print("{num:*>10.2f}".format(num=125.6115))


# string
# print("*******string*********")
# print("{:8s}".format("harry"))
# print("{:<8s}".format("harry"))
# print("{name:*<8s}".format(name="harry"))
# print("{name:>8s}".format(name="harry"))
# print("{name:*>8s}".format(name="harry"))
# print("{name:^8s}".format(name="harry"))
# print("{name:*^8s}".format(name="harry"))
#
# printing upto required letters of a string
# print("{:.3s}".format("Hariom kumar"))
# this means pura(:) ka(.) sirf 3 letter chahiye jo string hai
# print("{:8.3}".format("hariom kumar"))
# print("{:<8.3}".format("hariom kumar"))
# print("{:*<8.3}".format("hariom kumar"))
# print("{:>8.3}".format("hariom kumar"))
# print("{:*>8.3}".format("hariom kumar"))
#
# uses of , and _
# print("{:,}".format(2345678908765432456789))
# print("{:_}".format(2345678908765432456789))

# name = "hariom"
# age = 20
# print("my name is {} and my age is {}".format(name, age))
# here we have to maintain order.
# print("my name is {1} and my age is {0}".format(age, name))
#  by passing index no we can manage somehow

# a = 50
# b = 20
# print("{:.5}".format(a/b))

# using a tuple
# here we have to keep mind the index value
# accessing arguments item
# val=(10,20)
# print("{0[0]} {0[1]}".format(val))
# here 0 is position and [0][1] is the index no
# index of position


# using dict

# data = {"hariom": 21, "rahul": 48}
# print("rahul ka value {0[rahul]} and hariom ka value {0[hariom]}".format(data))
# print("hariom ka value {0[hariom]} and rahul ka value {0[rahul]}".format(data))

