# multilevel inheritance
# in multi level inheritance , the class inheritss the features of another erivedd class(child class)


'''

# multilevel inheritance with instance methods

class Father:
    def showF(self):
        print("this is father class inatance method")


class Son(Father):
    def showS(self):
        print("this is son class inatance method")


class Grand_son(Son):
    def showG(self):
        print("this is grand_son class inatance method")

# accessing all class instance method using grand_son object


g = Grand_son()
g.showF()
g.showS()
g.showG()

'''
'''


# multilevel inheritance with classmethods

class Father:
    fc = 'hariom'

    def showF(self):
        print("this is father class inatance method")

    @classmethod
    def father_cls(cls):
        print("This is class method in father class")
        print("value of class variable is ", cls.fc)


class Son(Father):
    sc = 'harry'

    def showS(self):
        print("this is son class inatance method")

    @classmethod
    def son_cls(cls):
        print("This is class method in son class")
        print("value of class variable is ", cls.sc)


class Grand_son(Son):
    gs = 'hmmm'

    def showG(self):
        print("this is grand_son class inatance method")

    @classmethod
    def grand_son_cls(cls):
        print("This is class method in Grand_son class")
        print("value of class variable is ", cls.gs)


# accessing all class methods using grand son object


g = Grand_son()
# accessing instance methods
g.showF()
g.showG()
g.showS()

print()
# accessing class methods
g.father_cls()
g.son_cls()
g.grand_son_cls()

'''


'''


# accessing all static methods
class Father:
    fc = 'hariom'

    def showF(self):
        print("this is father class inatance method")

    @classmethod
    def father_cls(cls):
        print("This is class method in father class")
        print("value of class variable is ", cls.fc)

    @staticmethod
    def staticF():
        print("this is father class static method")


class Son(Father):
    sc = 'harry'

    def showS(self):
        print("this is son class inatance method")

    @classmethod
    def son_cls(cls):
        print("This is class method in son class")
        print("value of class variable is ", cls.sc)

    @staticmethod
    def staticS():
        print("this is son class static method")


class Grand_son(Son):
    gs = 'hmmm'

    def showG(self):
        print("this is grand_son class inatance method")

    @classmethod
    def grand_son_cls(cls):
        print("This is class method in Grand_son class")
        print("value of class variable is ", cls.gs)

    @staticmethod
    def staticG():
        print("this is grand son class static method")


# accessing all class methods using grand son object


g = Grand_son()
# accessing instance methods
g.showF()
g.showG()
g.showS()

print()
# accessing class methods
g.father_cls()
g.son_cls()
g.grand_son_cls()
print()
# accessing static methods
g.staticF()
g.staticS()
g.staticG()
'''

'''
# multilevel inheritance , accessing constructors of all class in grand_son class

class Father:
    def __init__(self):
        print("this is father class constructor")

    def showF(self):
        print("This is father class instance method")


class Son(Father):
    def __init__(self):
        super().__init__()
        print("this is son class constructor")

    def showS(self):
        print("This is son class instance method")


class Grand_son(Son):
    def __init__(self):
        super().__init__()
        print("this is Grand_son class constructor")

    def showG(self):
        print("This is Grand_son class instance method")

# calling all constructors using grand_son object

# by using super method we can easily access all construcrs in  grand son  class


g = Grand_son()
print()
g.showF()
g.showS()
g.showG()

'''
