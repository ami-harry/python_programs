# tech package--> work module
# we are importing the User pack inside the Tech package and using the module of User package in this tech package
#
# from User import profile


def tech_work():
    print('tech package--> work module')
    print("tech_work() function")
    print()


# profile.user_profile()

# we cant run this in the same directry or using python3 filname.py
# we have to go to main folder then by using  flag method we have to run this file
# -m flag will be used to run this with directory only not with .py extension
# ex- python -m package_name.module_name
