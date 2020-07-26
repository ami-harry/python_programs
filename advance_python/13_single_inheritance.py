# Inheritance

# the mechanism of deriving a new class from an old one (existing class) such that the new class inherit all members (varibles and members) of old class is called inheritance or derivation.

# super class and  sub class
# the old class is referred as the super class and the new class is referred as sub class

# parent class--> super class, old class, base class
# child class--> sub class, new class, derived class


# all classes in python are build from a single super class called 'object'. so whenever we create a class in python, object will become super class for them internally.
# class Mobile(object):
# class Mobile():

# the  main advantage is code reusability

# types of inheritance:
# a. single inheritance
# b. multi-level inheritance
# c. herirachy inheritnce
# d. multiple inheritance


# decleration of child class
# class child_class_name(parent_class_name):
#            member of child class


# a. single inheritance
# if a class is derived from one base class(parent) , it is called sigle inheritance


# parent class
class Father:
    money = 14223  # class variable of parent class

    def ins_met_father(self):  # instance method of class variable
        print("instane method of father class")

    @staticmethod
    def static_method():
        business = 'yes'
        print("static method inside parent class :", business)
    # class method of parent class

    @classmethod
    def show_money(cls):
        print("money in parent class:", cls.money)


# child class
class child(Father):  # child class with the inheritance of father class
    car = 'yes'  # class variable of child class

# constructor of child class
    def __init__(self):
        money = 543212
# instance method of child class

    def show_money_child(self):
        print("money in child class:", self.money)

# class method of child class
    @classmethod
    def is_car(cls):
        print("car in child class:", cls.car)

# static method inside child class
    @staticmethod
    def stat_child():
        print("this is static method in child class")


# we can access all father class members and child class members using child class object
# we can access all father class members using father class object  but can't with child class object
#


c = child()  # child class member
print(c.car)  # accessing the class variable of child class using child object
c.show_money_child()  # accessing the instance method of child class using child object
c.is_car()  # accessing the classmethod of child class using child object
c.stat_child()  # accessing the static method of child class using child object
print()
# accessing the members of parent class using child object

print(c.money)  # accessing the class variable of parent class using child object
c.ins_met_father()  # accessing the instance method of father class using child class object
c.static_method()  # accessing the static method of father class using child class object
c.show_money()  # accessing the class method of father class using child class object


# if the method name in child class and parent class, and we are acessing it using child object,, it will give more precidence to child class method

# we can acess members of parent using parent object but not with child object
print()
fat_obj = Father()  # object of father class
print(fat_obj.money)  # printing class variable using class object
fat_obj.ins_met_father()
fat_obj.static_method()
fat_obj.show_money()
