# Interface
# in python, the interface concept is not explicitly available, like available other language like java
# in python, an interface is an abstract class which contains only abstract methods but not a single concrete method

'''
# this is an interface with only @abstract method nothing else
from abc import ABC, abstractmethod
class Fater(ABC):
    @abstractmethod
    def disp1(self):
        pass

    @abstractmethod
    def disp2(self):
        pass

    @abstractmethod
    def disp3(self):
        pass


'''
# if write any concrete method inside then it will work but will behave/work like abstract class, not as an interface

# rules
# all methods of an interface is abstract
# we can not create an object of interface
# if a class is implementing an interface if has to be define in all the methods given in that interface
# if a classs does not implement all the methods declare in the interface . the class must be declare abstrat


'''
# sample format of interace with inheritance concept

from abc import ABC, abstractmethod


class Father(ABC):
    @abstractmethod
    def fun1(self):
        pass

    @abstractmethod
    def fun2(self):
        pass

    @abstractmethod
    def fun3(self):
        pass
# here n no of abstract can take place, if only abstract method is there then it is an interface, otherwise it will be called as abstract class

# definig all the abstract methods in theirs respect childs


class child1(Father):
    def fun1(self):
        print('child1 class')
        print('definiting the abstract class of father class')


class child2(child1):
    def fun2(self):
        print('child 2 class')
        print('definiting the abstract class of father class')


class child3(child2):
class child3(child2):
    def fun3(self):
        print('child 3 class')
        print('definiting the abstract class of father class')
# by making child3 object we can access all the methods,


ch3 = child3()
ch3.fun1()
print()
ch3.fun2()
print()
ch3.fun3()
print()

'''


# example of this interface is in harry_ex_07.py

# trying to import this file here using import module concept


# here we have imported all the class of of the we will access that file using making its object
# these are the objectsm if any constructor , it will execute, we wll access the methods using this object
from harry_ex_07 import Army, Navy, AirForce
obj1 = Army()
obj2 = AirForce()  # these are the objectsm if any constructor , it will execute, we wll access the methods using this object
obj3 = Navy()  # these are the objectsm if any constructor , it will execute, we wll access the methods using this object

# accessing all the methods
obj1.area()
print()
obj1.dress()
print()
obj1.gun()
print()
obj1.salary()
print()
obj2.area()
print()
obj2.dress()
print()
obj2.gun()
print()
obj2.salary()
print()
obj3.area()
print()
obj3.dress()
print()
obj3.gun()
print()
obj3.salary()


