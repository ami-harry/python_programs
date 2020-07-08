# faulty computer
# it will give wrong  calculations for some conditions
# +,-,*,/
# if 56+9=366, 73-6=234, 9*12=433, 89/4=421
#  a and b ko input lena hai
# ask krna hai kya kroge +,-,*,/

print("\t\t\tWelcome to Harry's faulty calculator\n")
print("Choose what you want to do")
num = int(input(
    "for addition\n2 for substraction\n3 for multiplication\n4 for division\n"))
print(num)

if(num == 1):
    a = int(input("Enter first number:"))
    b = int(input("Enter second number:"))
    if (a == 56 and b == 9):
        print('addition is 366')
    else:
        print("addition is ", a+b)

if (num == 2):
    a = int(input("Enter first number:"))
    b = int(input("Enter second number:"))
    if (a == 73 and b == 6):
        print('the dfference is 234')
    else:
        print("the difference is ", a-b)

if (num == 3):
    a = int(input("Enter first number:"))
    b = int(input("Enter second number:"))
    if (a == 9 and b == 12):
        print('multiplication is 433')
    else:
        print("multilpication is ", a*b)

if (num == 4):
    a = int(input("Enter first number:"))
    b = int(input("Enter second number:"))
    if a < b:
        print("second number can't be greater than first no\n", a, b)
    elif (a == 89 and b == 4):
        print('division is 421')
    else:
        print("division is ", a/b)
print("thanks for using faulty calculator")
