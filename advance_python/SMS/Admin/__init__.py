# Admin package--> __init__ module

# supposs in our admin package 1000 of modules are there, while importing using * we are importing all, this is not good for our program, so we will make a list of only important modules and only those modules will be imported using *


__all__ = ['service', 'product']
