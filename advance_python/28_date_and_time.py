# date and time
# following modules are used to work with date, time and duration
# time
# datetime


# EPOCH
# the EPOCH is the point where the time starts, and is a plateform dependent. this point is taken as the january 1st of the current year, 00:00:00, for UNIX the epoch is January 1st 1970,00:00:00 UTC

# UTC
# UTC is coordinated universal time (formely known as greenwish means time or GMT). the acrony UTC is not a mistake but a compromision between English and French

# DST
# DST is daylight saving time, an adjustment of the timezone by (usually) one hour duration part of the year. DSt rules are magic(detemined by local law) and can change from year to year.

# time module
# time() function
# this funtion returns the time in seconds since the epochas a floating point number. the specific date of the epoch and the handling of leap seconds is plateform dependent

# ctime() function
# this function is used to get current date and time when we pass epoch time in seconds for the function, it returns corresponding date and time in string format. when we do not pass epoch time, it returns current date and time in string format

# localtime() function
# this function is used to convert seconds into date and time, it returns an object struct_time which can be used to access the attrubute either using an index or using a name

# index     attribute            value
#   0       tm_year         4 digit year number e.g.. 2020
#   1       tm_mon          Range[1,12]
#   2       tm_mday         Range[1,31]
#   3       tm_hour         Range[0,23]
#   4       tm_min          Range[0,59]
#   5       tm_sec          Range[0,61] , including leap seconds
#   6       tm_wday         Range[0,6], Monday is 0
#   7       tm_yday         Range[1,366]
#   8       tm_isdst        [0,1 or -1], 0=no DST, 1=DST is in effect, -1= not known
#           tm_zone       timezone name
#           tm_gmtoff     offset east of UTC in seconds


# we are importing only useful function
from time import time, ctime, localtime
'''
a = time()  # it will return the date time in seconds
print(a)
# we will change the returned seconds into a readable time format using ctime
ot = ctime(a)  # storing the original time returned by ctime into ot
print(ot)

# printing directly
print()
print(time())
print()
print(ctime())
print()
print(ctime(time()))  # will also return the current time

'''


# localtime--> it will return a list of attribues , we can accesss the attributes using variable

st = localtime()
print(st)  # it will print a list
# printing the list attribute

print(st.tm_year)
print(st.tm_mon)
print(st.tm_mday)
print(st.tm_hour)
print(st.tm_min)
print(st.tm_sec)

# printing with a valid

print("Year", st.tm_year)
print("Month", st.tm_mon)
print("Day", st.tm_mday)
print("Hour", st.tm_hour)
print("Min", st.tm_min)
print("Sec", st.tm_sec)
#
print()
print("Indin format")
print(st.tm_mday, end='/')
print(st.tm_mon, end='/')
print(st.tm_year, end='  ')
print(st.tm_hour, end=':')
print(st.tm_min, end=':')
print(st.tm_sec)
print(st.tm_zone)
print(st.tm_gmtoff)  # this will show the original time of UNIX
print(ctime(st.tm_gmtoff))  # this will show the original time of UNIX
a = 234567894576  # a random num suppose as seconds
print(ctime(a))  # it will convert in into a readable format
