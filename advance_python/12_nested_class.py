# nested class
# a class inside class

# outer class
class Army:
    # constructor of outer class
    def __init__(self):
        self.name = 'harry'
        # creating object of inner class inside the constructor of outer class
        self.gn = self.Gun()

    # outer class method
    def show(self):
        print("name:", self.name)

    # inner class
    class Gun:
        # constructor of inner class
        def __init__(self):
            self.name = 'AK47'
            self.capacity = '75 rounds'
            self.length = '33.35 inch'

        # inner class method
        def disp(self):
            print("gun name:", self.name)
            print("gun capacity:", self.capacity)
            print("gun length:", self.length)


# creating object of outer class
a = Army()
print(a.name)  # accessing variable of outer class
a.show()  # accessing the method of outer class
print()
# we cannt access the variable and method of innner class directly. we have to maintain proper location or path

# accessing inner class variable, we can store it into a variable and can print directly
print(a.gn.name)  # accessing the variable of inner class
# the path is ,, object_of_outer class.object_inner_class.var_of_inner_class
print()
ab = a.gn  # storing the path in a variable, we can access the variable after writing after it
print(ab.name)
print(ab.capacity)
print(ab.length)
print()
ab.disp()  # calling the function
print()
# accessing the method of inner class directly(without storing into a variable)
a.gn.disp()


# we can create object of inner class outside the class also like this
print()
obj_in_cls = Army().Gun()
# obj_in_cls is the new object of inner class Gun
# printing values using this object
print(obj_in_cls.name)
print()
obj_in_cls.disp()
