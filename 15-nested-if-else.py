# in nested if-else statement, an entire if-else construct is written within either the bosy of the if statement or the body of the else statement.

a=int(input("enter the first value"))
b=int(input("enter the second value"))
c=int(input("enter the third value"))
d=int(input("enter the forth value"))

if a>b:
    print("a is greater than b",a,b)
    if b>c:
        print("b is greater than c",b,c)
    else:
        print("c is less than b",c,b)
else:
    if c>d:
        print("c is greater than d",c,d)
    else:
        print("d is greater than c ",d,c)
print("rest of code")