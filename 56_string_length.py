# index
# it represents the no of characters in the string
# ex- str1="harry"
# index starts from  0

# accessing character and string
# there is no seperate concept of character in the string. we use the operations of char using string operation

str1 = "Harry"
print("Accessing the string character using index no :")
print("Value at index no 0 is ", str1[0])
print("Value at index no 1 is ", str1[1])
print("Value at index no 2 is ", str1[2])
print("Value at index no 3 is ", str1[3])
print("Value at index no 4 is ", str1[4])

print()
print("The string is ", str1)
print()

# string length
# length of string represents the no  of character in a string.
# len() function is used to get lenth of strings.

str3 = "Hariom"
print("The length of string ", str3, " is ", len(str3))
print()

# taking input from the user and printing the length of the string
inp_str = input("Enter your string to find lenth:")
print()
print("You have entered ", inp_str, " and its lengh is ", len(inp_str))
print()
print("Printing you string using index or character by character: ")
print()
for char in range(len(inp_str)):
    print("Charcater at index no ",char ," is ",inp_str[char])

