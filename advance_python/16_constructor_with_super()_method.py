# constructor with super method()
# if wee write constructor in both classes, parent and child class, then the parent class constructor is not available to the child class
# in this case only child class constructor is accessible whcih means child class constructor is replacing present child constructor
# super() method is used to call parent class constructor or methods from the child class


'''
# constructor with super class without parameter
class Father:
    def __init__(self):
        self.name = 'hariom'
        print("father class constructor is calling")

    def show(self):
        print("parent class instance method")


class Son(Father):
    def __init__(self):
        super().__init__()  # here we are using super method, it will make to call both constructors
        print("child class constructor is calling")

    def disp(self):
        print("child class instance method")


c = Son()  # here by using super method, both constructor will be called
c.show()
c.disp()
print(c.name)


'''

# constructor with super class with parameter


class Father:
    def __init__(self, name):
        self.name = name  # parent class instancce variable
        print("Parent class constructor is calling")

    def show(self):
        print("parent class instance method is calling")


class Son(Father):
    def __init__(self, name, roll):
        super().__init__(name)
        self.roll = roll  # child class instancce variable
        print("child class constructor is calling")

    def disp(self):
        print("child class instance method is calling")
        print("passed name is ", self.name)
        print("passed roll is ", self.roll)


'''
s = Son('hariom', 21)
s.show()
s.disp()

'''


'''
# we can pass a list in actual argumet too
a = ['hariom', 'harry', 'hk']
b = [32, 56, 23, 87]


s = Son(a, b)
s.show()
s.disp()

'''
