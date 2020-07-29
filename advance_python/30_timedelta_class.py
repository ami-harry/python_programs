# timedelta class
# timedelta class represents a duration , the difference between two dates or time.

# it is possible to know the future date or previous date using timedelta

# creating object of timedelta class
# object_name(days=0,seconds=0,microsecond=0,millisecond=0,minute=0, hour=0,week=0)
# all arguments are optional and default to zero, argument may be integer or floats and may be positive or negative
# all day second and microseconds are stored internally are converted to those units.
# a millisecond is converted to 1000microsecond
# a minute is converted into 60 seconds
# a hout is converted into 3600 seconds
# a week is convrted into 7 days


from datetime import timedelta, date

dl = timedelta(days=20)
tod = date.today()  # it wil return today date
print("Today is ", tod)
print("20 days after", tod+dl)
print("20 days before", tod-dl)
