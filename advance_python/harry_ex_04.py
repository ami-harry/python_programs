# make multilevel inheritance
# with parameter and access class, static , instance method and constructrs with parameter

class Father:
    fcv = 'father class value'

    def __init__(self, v):
        super().__init__(v)
        self.value = v
        print("Constructor of father class")
        print("Value :", self.value)

    def showF(self, n):
        self.namef = n
        print("Instance method of father class")
        print("value  :", self.namef)

    @classmethod
    def classF(cls, cv):
        cls.namef = cv
        print("Class method of father class")
        print("value ", cls.fcv)
        print("value:", cls.namef)

    @staticmethod
    def staticF(f):
        valuef = f
        print("Static method of father class")
        print("value :", valuef)


class Mother:
    mcv = 'mother class value'

    def __init__(self, v):
        super().__init__()
        self.value = v
        print("Constructor of mother class")
        print("value:", self.value)

    def showM(self, m):
        self.namem = m
        print("Instance method of mother class")
        print("Value: ", self.namem)

    @classmethod
    def classM(cls, m):
        cls.namem = m
        print("Class method of Mother class")
        print("value:", cls.namem)
        print("Value: ", cls.mcv)

    @staticmethod
    def staticM(m):
        valueM = m
        print("Static method of mother class")
        print("Value: ", valueM)


class Son(Father, Mother):
    scv = 'harry'

    def __init__(self, v):
        self.value = v
        super().__init__(v)
        print("this is contsructor of son class")
        print("value:", self.value)

    def showS(self, s):
        self.names = s
        print()
        print("Instance method of son class")
        print("father value  :", self.namef)
        print("mother value  :", self.namem)
        print("Son value: ", self.names)

    @classmethod
    def classS(cls, s):
        cls.names = s
        print("Class method of son class")
        print("value:", cls.namef)
        print("value:", cls.namem)
        print("value:", cls.names)
        print()
        print('clas variable')
        print('father', cls.fcv)
        print('mother', cls.mcv)
        print('son', cls.scv)

    @staticmethod
    def staticS(s):
        values = s
        print("static method of son class")
        # print("value:", valuef) # we cant access thge static value of another class
        # print("value:", valuem)
        print("value:", values)


s = Son('hello')  # calling the contructors
print()
s.showF('father')
print()
s.showM('mother')
print()
s.showS('Harry')
print()
s.classF('father class')
print()
s.classM('mother class')
print()
s.classS('son class')
print()
s.staticF('static of father')
print()
s.staticM('static of mother')
print()
s.staticS('static of son')
print()

print(s.fcv)
print(s.mcv)
print(s.scv)
