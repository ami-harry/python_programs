# Abstract class
# a class derived from ABC class which belongs to abc module is known as abstract class in python
# ABC class is known as Mets class which means a class that defines the behaviour of other class. so we can say Meta class ABC defines that the class which is derived from it becomes an abstract class
# abstract class can have abstract method and concrete methods
# abstract class needs to be extended and aits method implementation
# PVM can not create object of an abstract class
# ex--> from acb import ABC, abstractmethod
# class Father(ABC)

# Abstract method
#  a abstract method is a method whose action is redefined in the child classes as per the requirement of the object
# we can declare a method as abstract method using @abstractmethod decorator
# ex-->
# from abc import ABC, abstractmethod
# class Father(ABC):
#   @abstractmethod
#   def disp(self):
#       pass


# Concrete method
# a concrete method is a method whose action is defined in the abstract class itself
# ex-->
# from abc import ABC, abstractmethod
# class Father(ABC): #abstract method/method without body
# @abstractmethod
# def disp(self):
# pass
#
# def show(self): #concrete method/method with body
# print("Concrete mothod")


# rules:
# PVM can not create objects of an abstract class
# it is not necessary to declare all methods abstract in a abstract class
# abstract class can have abstract method and concrete method
# if there is any abstract method in a class, that class must be abstract
# the object methods of an abstract class must be defined in its child class/subclass
# if you are inheriting any abstract class that have abstract method, you must either provide the implemenetation of the method to make this class abstract.

# we use abstract class when there are some common features shared by all the objects as they are


# defence Force
# gun= AK47
# area=


# Army
# gun=AK47
# area=land

# Navy
# gun=AK47
# area=sea

# air_force
# gun=AK47
# area =sky

# gun is the common features shared by all forces but area is different for them.


# basic example of abstract method and abstract class
'''
from abc import ABC, abstractmethod


class Father(ABC):
    @abstractmethod
    def disp(self):
        pass  # we will define this abstract method in child class

    def show(self):
        print("this is concrete method")
# we cant make object for abstract class

# making its child and defining abstract method


class Child(Father):
    def disp(self):
        print("child class")
        print("abstract method definition")


# creating its object and accesing abstract method
c = Child()
c.disp()
print()
c.show()

'''
'''


# basic example of abstract method and abstract class with constructor
from abc import ABC, abstractmethod


class Father(ABC):
    def __init__(self, val):
        self.value = val
        print("abstract/father class constructor")
        # parameter value will be printed
        print("value of construcor is:", self.value)

    @abstractmethod
    def disp(self):
        pass  # we will define this abstract method in child class

    def show(self):
        print("this is concrete method")
# we cant make object for abstract class

# making its child and defining abstract method


class Child(Father):
    def __init__(self, val):
        self.value = val  # if we give any default value, it will skip the argument value
        super().__init__(val)
        print("child class constructor")
        print("value of child class constructor is ", self.value)

    def disp(self):
        print("child class")
        print("abstract method definition")


# creating its object and accesing abstract method
c = Child('hariom')
# c.disp()
# print()
# c.show()

'''
# more operations are in harry_ex_06.py


# make a perfect example of abstract class and method

from abc import ABC, abstractmethod

class DefenceForce(ABC):
    def __init__(self):
        self.val = 'proud be an indian'

    @abstractmethod
    def area(self):
        pass #we will define the area in its childs class
    
    def gun(self):
        print("Gun=AK47")

    
class Army(DefenceForce):
    def __init__(self):
        print("this is army constructor")
        super().__init__()
        print(self.val) #calling the value of parent constructor
    # defining the abstract method here
    def area(self):
        print("this is army abstract method definition")
        print("Area=Land")

class AirForce(DefenceForce):
    def __init__(self):
        print("this is airforce constructor")
        super().__init__()#calling the value of parent constructor
        print(self.val)

    # defining the abstract method here
    def area(self):
        print("this is airforce abstract method definition")
        print("Area=Sky")


class Navy(DefenceForce):
    def __init__(self):
        print("this is navy constructor")
        super().__init__()#calling the value of parent constructor
        print(self.val)
    # defining the abstract method here
    def area(self):
        print("this is navy abstract method definition")
        print("Area=Sea")



# creating childs objct and calling the abstract method

a=Army() #here the constructor will be called
print()
af=AirForce() #here the constructor will be called
print()
n=Navy() #here the constructor will be called
print()
# printing or accessing abstract method
a.area()
a.gun()
print()
af.area()
af.gun()
print()
n.area()
n.gun()
print()