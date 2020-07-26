# multilevel inheritance with parameter
# accessing all instance methd, constructors, class methods, and static methods

class Father:
    fcv = 'harry'

    def __init__(self, v):
        self.value = v
        print("this is constructor of father class ")
        print("value of constructor variable is ", self.value)

    def showF(self, f):
        self.class_name = f
        print("this is instance method of father class")
        print("actual argument was:", self.class_name)

    @classmethod
    def classF(cls, name):
        cls.name = name
        print("This is class method of father class")
        print("value of class variable is ", cls.fcv)
        print("actual argument was:", cls.name)

    @staticmethod
    def staticF(val):
        value = val
        print("this is static method of father class")
        print("actual argument was:", value)


class Son(Father):
    scv = 'hariom'

    def __init__(self, v):
        super().__init__(v)
        print("this is constructor of son class ")
        print("value of constructor variable is ", self.value)

    def showS(self, f):
        self.class_name = f
        print("this is instance method of son class")
        print("actual argument was:", self.class_name)

    @classmethod
    def classS(cls, name):
        cls.name = name
        print("This is class method of son class")
        print("value of class variable is ", cls.fcv)
        print("actual argument was:", cls.name)

    @staticmethod
    def staticS(val):
        value = val
        print("this is static method of son class")
        print("actual argument was:", value)


class Grandson(Son):
    gcv = 'hk'

    def __init__(self, v):
        super().__init__(v)
        print("this is constructor of son class ")
        print("value of constructor variable is ", self.value)

    def showG(self, f):
        self.class_name = f
        print("this is instance method of Grand_son class")
        print("actual argument was:", self.class_name)

    @classmethod
    def classG(cls, name):
        cls.name = name
        print("This is class method of Grand_son class")
        print("value of class variable is ", cls.fcv)
        print("actual argument was:", cls.name)

    @staticmethod
    def staticG(val):
        value = val
        print("this is static method of Grand_son class")
        print("actual argument was:", value)

# calling all methods using grand son object


g = Grandson(1000)  # here we are calling all constructor with argument
print()
# accessing all instance methods and passing class name to see where it is accessing
g.showF(Father)
print()
g.showS(Son)
print()
g.showG(Grandson)
print()
# passing a string as its parameter
g.showF('Hariom')
print()
g.showS('Harry')
print()
g.showG('hk ')
print()
# accessing all class variables
print(g.fcv)
print(g.scv)
print(g.gcv)
print()
# accessing all class methods and passing the class as its argument  to see  from where it is executing
g.classF(Father)
print()
g.classS(Son)
print()
g.classG(Grandson)
print()
# passing an string as actual argument at calling the class method
g.classF('Hariom')
print()
g.classS('Harry')
print()
g.classG('Hk')
print()
# accessing all static method and passing the class name as its argument
g.showF(Father)
print()
g.showS(Son)
print()
g.showG(Grandson)
print()
# passing an string as actual argument at calling the static method
g.showF('Hariom')
print()
g.showS('Harry')
print()
g.showG('Hk')
print()
