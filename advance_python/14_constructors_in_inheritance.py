# constructor in inheritance


# by default the constructor in the parent class in available in the child class

# in these examples the classes have only one constuctor and only one methods


'''
# father class without parameter
class Father:
    business = 'yes'  # class variable of parent class

    def __init__(self):  # constructor if parent class
        self.car = 'yes'
        print("constructor is called in parent class")

    # instance method in parent class
    def show(self):
        print("car in parent class:", self.car)

    @classmethod
    def is_buss(cls):
        print("business in parent class:", cls.business)


# child class
class Child(Father):
    def child_show(self):
        print("car in child class from father class is :", self.car)

    @classmethod
    def child_is_bus(cls):
        print("Business in child class from father is :", cls.business)


# creating object of child class and accessing all the members of child and father class

c = Child()  # here constructor is called
print(c.business)  # calling the parent class variable using child object
c.show()  # calling the parent class instance method using child object
c.is_buss()  # calling the parent class method using child object

print()

c.child_is_bus()
c.child_show()


'''

# with parameter


class Father:
    cv = 'this is class variable'

    def __init__(self, m):
        self.money = m
        print('parent constructor is calling')

    def show(self):
        print("money through parent instance method", self.money)

    @classmethod
    def cls_met(cls):
        print("class variable through class method", cls.cv)


class Son(Father):
    def show_money(self, c):
        self.car = c
        print('money is child class through father class is ', self.money)
        print("this is inside son class", self.car)

    @classmethod
    def ch_cls(cls):
        print("class variable through child class", cls.cv)


s = Son(1234)  # passing argument for parent constructor
s.show()  # accessing parent instance method using child object
s.cls_met()  # accessing class method of parent using child object
s.show_money('yes')  # passing the argument for child class instane method
s.ch_cls()  # calling the child class method using child class object
print(s.car)
print(s.cv)
