# harry module --> this is our main file, here we will import all the packages and its modules


# importing with syntax
#  import module_name.package_name

# importing modules from another package
# import Admin.service  # here Admin is a package and we are importing its service module
# import Admin.product  # here Admin is a package and we are importing its product module

# accessing the module functions,classes, methods etc..
# here Admin is package name, servie is a module and admin_service is an function of service module
# Admin.service.admin_service()
# here Admin is package name, product is a module and admin_product is an function of product module
# Admin.product.admin_product()
#
#
# calling package inside package of its module
#
#
#
#
#
#


# here Admin is main package and inside it Common is another package and footer is its module
# import Admin.Common.footer
# here Admin is main package and inside it Common is another package and header is its module
# import Admin.Common.header


# accessing the function, method, class, var of package, inside package of its module
# accessing admin_common_footer function of footer module from Common package inside Admin package
# Admin.Common.footer.admin_common_footer()
# accessing admin_common_header function of header module from Common package inside Admin package
# Admin.Common.header.admin_common_header()

#
#
#
#
#


# accessing another package named Tech and its module and functions
# import Tech.profile  # here Tech is the package name profile is its module name
# import Tech.work  # here Tech is the work name profile is its module name

# Accessing the func, methods , claasses, var from Tech package of its modues

# here Tech is package, inside it profile is a module and we are accessing its function named tech_profile()
# Tech.profile.tech_profile()
# here Tech is package, inside it work is a module and we are accessing its function named work_profile()
# Tech.work.tech_work()
#
#
#
#
#


# accessing another package named User and its module and functions

# import User.profile  # here User is package and we are importing its module named profile
# import User.request  # here User is package and we are importing its module named request

# accessing the module functions, methods, vars of User package
# User.profile.user_profile() #here user_profile() is the function of profile module inside User package
# User.request.user_request() #here user_request() is the function of request module inside User package
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#

# importing with other syntax
# from package_name import module_name

# from Admin import service  # here from Admin package we are importing service module
# from Admin import product  # here from Admin package we are importing product module

# accessing the members of imported modules

# here service is the module name and admin_service() is the function we are accessing
# service.admin_service()
# here product is the module name and admin_product() is the function we are accessing
# product.admin_product()

#
#
#
#
#

# here from Admin package we are importing Common package and then from Common package we are importing header module
# from Admin.Common import header
# here from Admin package we are importing Common package and then from Common package we are importing footer module
# from Admin.Common import footer

# accessing the members of imported module
# here header is the module name we are importing its function
# header.admin_common_header()
# here header is the module name we are importing its function
# footer.admin_common_footer()

#
#
#
#
#

# importing with syntax
#  from package_name import module1, module2, ...
# here from Tech package we are importing profile module and work modules both
# from Tech import profile, work

# accessing the members of imported modules

# profile.tech_profile()  # here profile is the module and we are accessing its function
# work.tech_work()  # here work is the module and we are accessing its function

#
#
#
#
#

# here from User package we are importing request module and profile modules both
# from User import request, profile

# accessing the members of imported modules
# request.user_request()  # here request and we are accessing its function
# profile.user_profile()  # here profile and we are accessing its function

#
#
#
#
#

# we can also access with aliasing name tooooooooooooooooooooooooooooooooo

# from module_name import *
# this will not work with package, it works with modules only
# to make it work with package file, we have to make a list of module which we want to import using *,  we have to save it in __init__.py file, so that we can use this type of import syntax
# we have to specify that from package i want to access these these modules, and we will make a list of it, and that only modules will be only imported when we use this syntax

# this is very helpful for the program becuase if a package has 1000 of module and we need only few of them and using * we are importing all the modules, it will make our program slow processing, so we will make  a seperate list of imortant module in __init__.py file then will import using * those only important modules

# inside the __init__.py file we will make a list as
# __all__=[here we will write the names of modules which we want to import ]


#
#
#
#
#

# using the syntax
# from package_name import *
# before this ensure that we have crated a list of important modules inside our __init__.py file. only those modules will be accessible using *

# from Admin import *  # using * we are importing the list of modules of Admin package
# here service is the module name and we are accessing its function
# service.admin_service()
# here product is the module name and we are accessing its function
# product.admin_product()

#
#
#
#
#

# here we are imporiting important modules of Common package which is inside Admin package
# from Admin.Common import *

# accessing the imported modules members

# here footer is the module and we are accessing its function
# footer.admin_common_footer()
# here header is the module and we are accessing its function
# header.admin_common_header()

#
#
#
#
#

# here we are imporiting important modules of Tech package
# from Tech import *
# accessing the imported modules members
# profile.tech_profile()  # here profile is module and we are accessing its function
# work.tech_work()  # here work is module and we are accessing its function

#
#
#
#
#
# here we are imporiting important modules of User package
# from User import *
# accessing the imported modules members
# profile.user_profile()  # here profile is the module name we are accessing its function
# request.user_request()  # here request is the module name we are accessing its function

#
#
#
#
#


# importing all packages and its module

# from Admin import *
# from Admin.Common import *
# from User import *
# from Tech import *

# accessing the members of import modules

# these are the modules of packages Admin and we are accessing it function
# product.admin_product()
# these are the modules of packages Admin and we are accessing it function
# service.admin_service()

# here we are accessing the function of package Common inside Amdin package
# footer.admin_common_footer()
# here we are accessing the function of package Common inside Amdin package
# header.admin_common_header()

# here we are accessing the functions of module inside the Tech package
# profile.tech_profile()
# here we are accessing the functions of module inside the Tech package
# work.tech_work()

# here the profile module is matching in Tech and user packages
# so it will show an error so be careful of it
# here user profile will not be accssible becuas Tech is importing after the User
# so User profile will be replaced by Tech profile

# this will run, becuase in all imported package these is no module named request
# request.user_request()
# it will show an AttributeError that tech_profile has no attribute user,
# profile.user_profile()
# bacuse tech is importing after user and it will replace the same name modules,
# we can resolve this error using aliasing name for modules having same name
# by giving aliasing name we can access both or by using sepearte importing and accessing the module using its package name as well



