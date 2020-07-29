# formatting date and time
# strftime()--> this method is used to formaat the conent of datetime, date and time class object.strftime represents string format to time
# this method convert the object into a specified format and returns the formatted string


# https://docs.python.org/3/library/datetime.html


from datetime import datetime

dt = datetime.today()
print(dt)
print(type(dt))

print()
newd1 = dt.strftime('%B%d %Y')
print(newd1)
print()
newd2 = dt.strftime('%d/%b/%Y')
print(newd2)
print()
newd3 = dt.strftime('%b-%M-%Y')
print(newd3)
print()
newt1 = dt.strftime('%H:%M:%S')  # 24 hr format
print(newt1)
print()
newt2 = dt.strftime('%I:%M:%S')  # 12 hr format
print(newt2)
print()
