# user package--> request module module
# using the sibling concept
# using the module of another package inside the module of another package
# we are going to use work module of Tech package inside the request module of User package

# from package_name import module_name
# this is the syntax
# we can use * also(make sure that we have created a list inside the __init__.py file to access those modules)

# here we are importing profile module of Tech package
# from Tech import profile
#
# we can do this in other way too
# we can define the system path also and it will work as normal program work

# import work
# import sys
# sys.path.append('/home/harry/Desktop/geek_py/advance_python/SMS/Tech/')


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


# here we are accessing the function of profile module of Tech package
# profile.tech_profile()

# to run this program we have to go to main folder loaction and will type python3 -m pkg_name.mod_name
# python3 -m User.request --> it will work


# running through sys.path
# work.tech_work()
# it will work
