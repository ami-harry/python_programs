# Tech package--> __init__ module
# here we have to mention those module name which we want to import using *


__all__ = ['logout', 'profile', 'work']

# here we have only three modules in our package, but in case if we have 100 of modules in the package and we need only 10-15 of them. so if we import all then it is waste of memory and the program will also become slow, so we are making a list of important modules to import which is useful for us
