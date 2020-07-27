# make hierarchy inheritance
# with parameter and access class, static , instance method and constructrs with parameter

class Father:
    fcv = 'father class value'

    def __init__(self, v):
        self.value = v
        print("Constructor of father class")
        print("constructor value is in father class is :", self.value)

    def showF(self, n):
        self.name = n
        print("Instance method of father class")
        print("value of instance method in father class  is :", self.name)

    @classmethod
    def classF(cls, cv):
        cls.name = cv
        print("Class method of father class")
        print("value:", cls.name)
        print("The father class variable is ", cls.fcv)

    @staticmethod
    def staticF(f):
        valuef = f
        print("Static method of father class")
        print("value in father class method:", valuef)


class Son(Father):
    scv = 'son class value'

    def __init__(self, v):
        self.name = v
        super().__init__(v)
        print("Constructor method of son class ")
        print("constructor value is in father class is :", self.name)

    def showS(self, sm):
        self.inst = sm
        print("Instance method of son class")
        print("value of instance method in child class is ", self.inst)
        print("value of instance method in father class  is :", self.name)

    @classmethod
    def classS(cls, scv):
        cls.nick = scv
        print("Class method of son class")
        print("value in son class method:", cls.nick)
        print("value in father class method:", cls.name)
        print("The son class variable is ", cls.scv)
        print("The father class variable is ", cls.fcv)

    @staticmethod
    def staticS(sfv):
        value = sfv
        print("Static method of son class")
        print("value in son class static method:", value)


class Daughter(Father):
    dcv = 'daughter class value'

    def __init__(self, v):
        self.name = v
        super().__init__(v)
        print("Constructor method of daughter class ")
        print("constructor value is in father class is :", self.name)

    def showD(self, dm):
        self.inst = dm
        print("Instance method of daughter class")
        print("value of instance method in daughter class is ", self.inst)
        print("value of instance method in father class  is :", self.name)

    @classmethod
    def classD(cls, dcv):
        cls.nick = dcv
        print("Class method of daughter class")
        print("value in daughter class method:", cls.nick)
        print("value in father class method:", cls.name)
        print("The daughter class variable is ", cls.dcv)
        print("The father class variable is ", cls.fcv)

    @staticmethod
    def staticD(dfv):
        value = dfv
        print("Static method of daughter class")
        print("value in daughter class static method:", value)


# object of son class
# s = Son('harry')  # accessing constructor of son and father class
# print()
# s.showF('hk')  # calling the instance method of father class using son object
# print()
# s.showS('harry')  # calling the son instance method using son object
# print()
# s.classF('achha')  # calling the class method of father class using son object
# print()
# s.classS('hmmm')  # calling the class method of son class using son object
# print()
# calling the static method of father class using son object
# s.staticF('father class static method')
# print()
# calling the static method of son class using son object
# s.staticS('son class static method')
# print()
# print(s.fcv)  # accessing the father class variable using son object
# print(s.scv)  # accessing the father class variable using son object
#
# object of daughter class
d = Daughter('hello')  # accessing constructor of daughter and father class
print()
d.showF('this is father class instance method')
print()
d.showD('this is daughter class instance method')
print()
d.classF('this is father class class method')
print()
d.classD('this is daughter class class method')
print()
d.staticF('this is static method of father class')
print()
d.staticD('this is static method of daughter class')

print()
print(d.fcv)
print(d.dcv)
