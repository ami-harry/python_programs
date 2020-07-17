# take 2 string as input from the user and concitinate it , and ask how many times he wants to print it,
# find the length of the string and print the string charcaters by index value


str1 = input("Enter first string:")
str2 = input("Enter second string:")
str3 = str1+str2
print("The concatination of the string is ", str3)
print()

rep = int(input("Enter how many time you want to print the string: "))
print()
print(str3 * rep)
print("The length of the string is ", len(str3))
print()

print("the string charcaters as index place")

for data in range(len(str3)):
    print("Value at index no ", data, " is ", str3[data])
print()
print("out of loop")
