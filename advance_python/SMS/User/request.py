# user package--> request module module
# using the sibling concept
# using the module of another package inside the module of another package
# we are going to use work module of Tech package inside the request module of User package

# from package_name import module_name
# this is the syntax
# we can use * also(make sure that we have created a list inside the __init__.py file to access those modules)

# from Tech import *
# or
# here we are importing profile and work module from Tech package

# from Tech import profile


def user_request():
    print("user package--> request module")
    print("user_request() function")
    print()


# accessing the siblings module members
# module.function_name()
# here we are accessing the functionn of profile method  of Tech package
# profile.tech_profile()
# here we are accessing the functionn of work method  of Tech package
# work.tech_work()
