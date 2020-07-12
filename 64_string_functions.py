# string functions

# upper()
#   --> this method is used to convert all the strings into the uppercase.
# syntax --> string.upper()

# lower()
# --> this method is used to convert all the strings into the lowercase
# syntax --> string.lower()

# swapcase()
# -->this method will convert all uppercase to lower and lower to upper.
# syntax --> string.swapcase()

# title()
# --> this method will make first letter to upper case of all the string.
# syntax --> string.title()


# isupper()
# --> this method is used to test the given string is in upper case or not. if all elemets are in uppercase it returns True else false
# syntax- string.isupper()

# islower()
# --> this method is used to test the given string is in lower case or not. if all elemets are in lower case  it returns True else false
# syntax- string.islower()

# istitle()
# this method is used to test that the given string is i title format or not.
# if any starting letter of word in in lowercase then it will return False else True
# syntax --> string.istitle()


# isdigit()
# this method returns True if the string contains only numeric digit(0 to 9) else returns False.
# syntax--> string.isdigit

# isalpha()
# this method  is used to check that that the string has atleast one character and all are alphabets(A to Z or a to z) then returns True else False
# syntax--> string.isalfa

# isalnum()
# this method returns True if the string has atleast one character and all character in the string are alphaneumeric (a to or A to Z and 0 to 9) else returns False
# syntax--> string.isalnum()

# isspace()
# this method returns True if the string has space only else False
# syntax--> string.isspace()


# lstrip()
# this method will remove all the spaces which are at the left side of the string.
# syntax--> string.lstrip()

# rstrip()
# this method will remove all the spaces which are at the right side of the string
# syntax-->string.rstrip()

# strip()
# this method will remove all the spaces from the both side of the string
# syntax--> string.strip()


# replace()
# this method is used to replace a sub script in a string with another sub string.
# syntax--> string.replace(old,new)

# split()
# this method is used to split/break a string into pieces. those pieces returns as a list.
# string--> string.split('seperator')

# join()
# this method is used to join strings into a single string.
# syntax--> 'seperator'.join(string)

# startswith()
# this method is sued to check wether a string is starting with a substring or not. it returns True if the string is starting with the specified substring
# syntax--> string.startswith('specified string')

# endswith()
# this method ised to check wether a string is ending with a specified string or not. it returns True if the string ends with the specified sbustring
# syntax-->string.endswith("specified-string")


#
# str1 = "Harry kumar from sitamarhi bihar"
# print("the original string is ", str1)
# print(str1.upper())
# print()
# print(str1.lower())
# print()
# print(str1.swapcase())
# print()
# print(str1.title())
# print()
#
#
#
#
# har = "HARIOM "
# print(har)
# print()
# print(har.isupper())
# har = "HArioOm"
# print()
# print(har)
# print(har.islower())
# print()
# har = "Hariom Kumar "
# print()
# print(har)
# print(har.istitle())
#

#
# str1 = "2134567890"
# print(str1)
# print(str1.isdigit())
# str1 = "213454df67890"
# print(str1)
# print(str1.isdigit())
#
#
# str1 = "Hariom"
# print(str1)
# print(str1.isalpha())
#
# str1 = "ha32om"
# print(str1)
# print(str1.isalpha())
#
# str1 = "ha32sdhgjk32wubefenwijlekskhf4iwjnreioyf3wi4rnwiurjwnefkus3h423iury3i4uom"
# print(str1)
# print(str1.isalnum())
# in this string a space is these so it is not of isalnum type
# str1 = "ha32sdhgjk32wubefenwijlek skhf4iwjnreioyf3wi4rnwiurjwnefkus3h423iury3i4uom"
# print(str1)
# print(str1.isalnum())
#
# str1 = " "
# print(str1)
# print(str1.isspace())
# str1 = ". "
# print(str1)
# print(str1.isspace())
#
# no matter how many spaces does it have  it will return True but we put any other thing except space it will return False


#
# str1 = "       Hariom Kumar"
# print(str1)
# print(str1.lstrip())
#
# str1 = "Hariom Kumar                       "
# print(str1)
# print(str1.rstrip())
#
#
# str1 = "                Hariom Kumar                            "
# print(str1)
# print(str1.strip())


# har="Hello harry"
# old1="Hello"
# new1="Hi"
# print(har)
# harnew=har.replace(old1,new1)
# print(harnew)


# str1 = " this is hariom kumar"
# print(str1)
# str2 = str1.split('-')
# str1 = " this is hariom kumar"
# str3 = str1.split("/")
# str1 = " this is hariom kumar"
# str4 = str1.split('+')
# str1 = " this is hariom kumar"
# str1 = " this is hariom kumar"
# str5 = str1.split('_')
# print(str2)
# print(str3)
# print(str4)
# print(str5)


# str2=('this', 'is', 'a','string')
# str_join='+'.join(str2)
# str_join1='-'.join(str2)
# str_join2='_'.join(str2)
# str_join3=','.join(str2)
# print(str2)
# print(str_join)
# print(str_join1)
# print(str_join2)
# print(str_join3)


# str1="Hello harry how are you"
# print(str1.startswith("Hel"))
# print(str1.startswith("hel"))
# print(str1.endswith("ou"))
# print(str1.endswith("you"))
# print(str1.endswith("."))
