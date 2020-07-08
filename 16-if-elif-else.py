# if-elif
# to show a multi-way decision based on several decision. we use of-elif statement..
# in this here is no exit condition meanwhile if no condition is matched then there will be no ouptut..

#
# a=int(input("Enter the  number:"))
# b=int(input("Enter the  number:"))
# if a > b:
# print("a is greater than b")
# elif a < b:
# print("a is less than b")
# here there is no condition where we can show that the numbers are equal.so simply we will put an else in last

# a=int(input("Enter the  number:"))
# b=int(input("Enter the  number:"))
# if a > b:
# print("a is greater than b")
# elif a < b:
# print("a is less than b")
# else:
# print("a and b are equal")


day = input('enter the day:')
if (day == 'monday' or 'Monday'):
    print('today is', day)
elif (day == 'tuesday' or 'Tuesday'):
    print('today is', day)
elif (day == 'wednesday' or 'Wednesday'):
    print('today is', day)
elif (day == 'thursday' or 'Thursday'):
    print('today is', day)
elif (day == 'friday' or 'Friday'):
    print('today is', day)
elif (day == 'saturday' or 'Saturday'):
    print('today is', day)
elif (day == 'sunday' or 'Sunday'):
    print('today is', day)
else:
    print("Enter a valid day")
