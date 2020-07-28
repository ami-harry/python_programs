# Module
# a module is a file containing python definitions and statements
# a module is a file conatining group of variables , modules , functions, methods etc
# they are executed only at the first time the module name is encountered in an import statement
# the file name is the module name with the suffix .py append
# types of module
# a. user-defined
# b. built-in module(array, math,sys etc...)


# when and why use module
# assume that you are building a vary large project it will be very difficult to manage all logic within a single file so if you want to seperare your similar logic to a seperate file , you can use module
# it will not only seperate your logic but will help you to debug your code easily as you know which logic is defined in which module.
# when a module is developed , it can be reused in any program that need that module

# how to import module
# import statement is used to import modules

# syntax
# import module_name
# import module_name as alias_name
# from module_name import var, fun, method, class etc
# from module_name import var as alias_name, fun, method as alias_name, class etc
# from module import * (* means all var, class, module, fun etc)


# import module_name
# this does not enter the names of function defined in module directly in the current symbol table, it only enters the module name there
#
# how to access methods, functions, class and variable
# using the module_name you can access the function
# syntax
# module_name.fun_name(para1,para2,,)
# module_name.var_name


# when 2 modules having the same function name then this module is good approach to use

# import module_name as alias_name
# this does not enter the names of function defined in module directly in the current symbol table, it only enters the module name there, if the module name is followed by as, then the name folloing as is bound directly to the imported module
# how to access methods, functions, class and variable
# using the alias_name you can access the function
# alias_name.var
# alias_name.method()
# alias_name.fun()


# from module_name import fun, var,class, method
# there is a varient of the import statemenbt that imports from a module directly into the importing module symbol table
# how to access methods, functions, class and variable
# you can access function names directly by its name
# fun_name()
# method_name()

# from module_name import fun, var as alias_name,class, method as alias_name
# how to access methods, functions, class and variable
# you can access function names directly by alias_name
# alias_name()
#


# from module_name import *
# this imports all names except those beginning with an underscore(_)
# how to access methods, functions, class and variable
# you can access function names directly by its name
#  fun_name()
#  method_name()


# module search path
# when a module cal is imported, the intepreter first searches for a built-in module with that name. if not found then it searches for a file named cal.py in a list of directories given by variable sys.path
# sys.path is initialized from these location

# current directory
# if not forund then searches each directories in the shell variable PYTHONPATH
# if not found then searchs installation dependent default path
# PYTHONPATH is a list of  directory names with the same name syntax, as the shell variable PATH

# module manages file and packages manages folders
