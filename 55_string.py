# string
# string represents the group of charcters.
# string are enclosed in double quotes or single quotes. the str data type represents a string
# ex='harry', "harry"
# h="harry"

# creating string
# single quote
print()
str1 = 'hii'
print("String using single quote : \n", str1)
print()

# double quote
str2 = "hello"
print("String using double quote is : \n", str2)
print()

# triple single quote
# this  is useful to create strings which span into several lines
str3 = '''this is
hariom
and who
are
you'''
print("string using three single quote is : \n", str3)
print()


# triple double quote
# this  is useful to create strings which span into several lines
str4 = """this
is
 hariom
  and who
  are you"""
print("string using three double quote is : \n", str4)
print()

# double quote inside single quote
str5 = 'hello "harry" how are you'
print(" double quote inside single quote string is : \n", str5)
print()

# single quote inside double quote
str6 = "hello 'harry' how are you"
print(" singlw quote inside double quote string is : \n", str6)
print()
# we cann't use double quote inside double quote and single quote inside single quote

# raw string
# this is useful to nulify the effect of escape characters.
str7 = r"hii \nharry how are \tyou"
print("The raw string is : \n", str7)
print()

# memory allocation:
# memory is allocated for the values. if two variables having same value then thosw variables will be tagged with the same addess. both can acces the same data.
# if one variable is modified with new value, then new address will be allocated for the new value and old address is useless now, then it will be collected by garbage collector and after that the new address will be used later

str8 = "harry"
str9 = "harry"
print("the address of  str9 is ", id(str9), " and the value is ", str8)
print("the address of  str8 is ", id(str8), " and the value is ", str9)
print()
# updating the varible with new value

str10 = "hariom"
print("The address before modification of the str10",
      id(str10), " and the value is ", str10)

str10 = "harry"
print("The new address of str10 after modification ",
      id(str10), " and the new value is ", str10)
print()

