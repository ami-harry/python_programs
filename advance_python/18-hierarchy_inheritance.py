# hierarchy inheritance

# in this inheritance, here only one parent class and it has many child class
# every child class can access parent class member but one child's cant access member of other child


'''
# instance method access

class Father:
    def showF(self):
        print("instance method of father class")


class Son(Father):
    def showS(self):
        print("Instance method of son class")


class Daughter(Father):
    def showD(self):
        print("Instance method of daughter class")


s = Son()  # object of son class, it can access father and it own member but cant access member of daughter class

s.showF()
s.showS()
print()
d = Daughter()  # object of daughter class, it cant access son class but can acces memebr of parent class
d.showF()
d.showD()

'''

# instance methods and constructors


class Father:
    def __init__(self):
        print("constructor of father class")

    def showF(self):
        print("Instance method of father class")


class Son(Father):
    def __init__(self):
        super().__init__()  # calling father class constructor
        print("constructor of son class ")

    def showS(self):
        print("Instane method of son class")


class Daughter(Father):
    def __init__(self):
        super().__init__()  # calling father class constructor
        print("Constructor of daughter class")

    def showD(self):
        print("Instance method of daughter class")


s = Son()
s.showF()
s.showS()
print()
d = Daughter()
d.showF()
d.showD()


# same we can do for class method and static method
