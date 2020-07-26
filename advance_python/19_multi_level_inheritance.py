# multilevel inheritance
# if aclass derived from more than one parent class is known as mutilevel inheritance


'''
# instance method
class Father:
    def showF(self):
        print("This is father class instance method")


class Mother:
    def showM(self):
        print("This is mother class instance method")


class Son(Father, Mother):
    def showS(self):
        print("This is child class instance method")


s = Son()
s.showF()
s.showM()
s.showS()
'''
'''

# constructor
# to access all constructor we have to use super() method in every class


class Father:
    def __init__(self):
        super().__init__()
        print("this is father class constructor")

    def showF(self):
        print("This is father class instance method")


class Mother:
    def __init__(self):
        super().__init__()
        print("This is mother class constructor")

    def showM(self):
        print("This is mother class instance method")


class Son(Father, Mother):
    def __init__(self):
        super().__init__()
        print("this is son class constructor")

    def showS(self):
        print("This is child class instance method")


s = Son()
print()
s.showF()
s.showM()
s.showS()

'''

# method resolution order(MRO)
# in the multiple inheritance senario members of class are searched first in the current class , if not found the search continues into parent class in depth first, left then right manner without searching thr same class
# search for the child class before going to the parent class
# when a class is inherited from several class, it searches in the order from left to right in the parent class
# it will not visit any class more than once, which means a class in the inheritance heirarchy is traversed only once.
#
#
