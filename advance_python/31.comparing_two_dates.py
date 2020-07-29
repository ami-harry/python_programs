# comparing two dates
# we can compare date class and datetime class objects using ==,<,>,!=
# the comparision will return either True or False

from datetime import date

d1 = date(2019, 12, 24)
d2 = date(2014, 2, 4)
print(d1)
print(d2)
print()
print(d1 == d2)
print(d1 < d2)
print(d1 > d2)
print(d1 != d2)
