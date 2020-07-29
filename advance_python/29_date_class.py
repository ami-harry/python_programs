# date class
# date object--> A date object is an object containing information of year,month and day.
#
# creating object of date class
# obj_name=date(year,month,day)

# all arguments are required. arguments may be integers, in the following range
# MINYEAR<=year<=MAXYEAR
# 1<=month<=12
# 1<=day<=number of day in the given month and year
# ex--> d=date(year=2019,month=12,day=23) or d=date(2019,12,23)


# date class method
# today()--> this method is used to get the current date, it returns only date
# ex--> date.today()


'''
from datetime import date

d1 = date(year=2020, month=12, day=24)
print(d1)

d2 = date(2020, 11, 12)
print(d2)
print('year:', d2.year)
print('month', d2.month)
print('day', d2.day)

'''


# datetime module

# datetime--> it handles date and time. is has year, month,day , hour, minute, second, millisecond and tzinfo attributes

# data--> it handles date of georgian calander without taking timezone into consideratioon. it has year,month and day attributes
# time--> it handles time assuming that everyday has excactly 24X60X60 seconds. it has hour, minute, second, mocrosecond and tzinfo attributes
# timedelta--> it handles durations. the duration may be the difference between two date , time or datetime instance.


# datetime class
# datetime class--> a datetime object is a single objct containing all the information from a date object and a time object.

# creating object of datetime class
# object_name=datetime(year,month,day,hour=0,minute=0,second=0,microsecond=0,tzinfo=None,*,fold=0)

# the year, month and day argument are required ,tzinfo  may be None or an instace of tzinfo subclass. the remaining argument may be integers in the following ranges
# MINYEAR<=year<=MAXYEAR
# 1<=month<=12
# 1<=day<=number of day in the given month and year
# 0<=hour<24
# 0<=minute<60
# 0<=second<60
# 0<=millisecond<1000000
# fold in[0,1]

# ex--> dt= datetime(year=2019, month=6,day=29,hour=12,minute=3)

# the fold parameter specifies whether there was amy fold in time. a fold in time means a reverse back of the clock time. in countries following daylight saving time during the end of summer clocks are reverse back by 1 hour. this reverse is fold in time

#  * means a splat operator. using a splat operator a tuple can be unpacked and a time object can be consttruct out of the values from the tuple

'''
from datetime import datetime

dt = datetime(year=2020, month=12, day=7, hour=12, minute=23)
print(dt)
print(dt.year)
print(dt.month)
print(dt.day)
print(dt.hour)
print(dt.minute)

hk = datetime(2019, 12, 23)
print(hk)
print(datetime(2016, 6, 7, 8, 9, 32))
print(datetime.year)

'''


# datetime class method
# now() -> this method is usedful to get the current date and time. we can provide timezone information to this method. if the timezone is not provided, then it takes the local time zone/ it returns an object that contains date and time information in any timezone. we can use day , month, hour,minute, second

# datetime.now()

# today()--> this method is used to get the curremt date and time . it returns the date and time information
# datetime.today()
'''
from datetime import datetime

dt = datetime.now()
print(dt)
print(dt.year)
print(dt.month)
print(dt.day)
print(dt.hour)
print(dt.minute)
print(dt.second)
print(dt.microsecond)


df=datetime.today()
print(df.year)
print(df.month)
print(df.day)
print(df.hour)
print(df.minute)
print(df.second)
print(df.microsecond)
print(df.tzinfo)

'''