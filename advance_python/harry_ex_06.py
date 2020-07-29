# basic example of abstract method and abstract class with constructor and classmethod, static method and instance method


from abc import ABC, abstractmethod


class Human(ABC):
    hcv = 'human'

    def __init__(self, valh):

        self.valueh = valh
        print("Constructor of Human class")
        print("value:", self.valueh)

    @abstractmethod
    def gender(self):  # this is abstract method and it will be defined in the child class
        pass

    def showH(self, nameh):
        self.name = nameh
        print("instance method of Human class")
        print("instance value:", self.name)

    @classmethod
    def classH(cls, clsH):
        cls.class_value = clsH
        print("this is class method of human class")
        print("the class variable value is ", cls.class_value)
        print("human class variable is :", cls.hcv)

    @staticmethod
    def statH(st):
        static_var_h = st
        print("this is static method")
        print("value:", static_var_h)


class Male(Human):
    mcv = 'male'

    def __init__(self, valh):
        print("this is Male class constructor method")

    def showM(self, m):
        self.male = m
        print('this is instance method of male class')
        print("value:", self.male)
        print("value of human class:", self.name)

    def gender(self):  # defining the abstract method
        print('Gender=Male')

    @classmethod
    def classM(cls, m):
        cls.male_class_var = m
        print("This is male class classmethod")
        print("classmethod variable is ", cls.male_class_var)
        print("value of male class variable is ", cls.mcv)
        print("value of human class variable is ", cls.hcv)

    @staticmethod
    def statM(m):
        male = m
        print("This is static method of male class")
        print("value:", male)


class Female(Human):
    fcv = 'female'

    def __init__(self, valh):
        print("this is female class constructor method")

    def showF(self, m):
        self.female = m
        print('this is instance method of female class')
        print("value:", self.female)
        print("value of human class:", self.name)

    def gender(self):  # defining the abstract method
        print('Gender=female')

    @classmethod
    def classF(cls, m):
        cls.female_class_var = m
        print("This is female class classmethod")
        print("classmethod variable is ", cls.female_class_var)
        print("value of female class variable is ", cls.fcv)
        print("value of human class variable is ", cls.hcv)

    @staticmethod
    def statF(m):
        female = m
        print("This is static method of female class")
        print("value:", female)


m = Male('hariom')  # here the constructor will be called
print()
f = Female('female')  # here the constructor will be called

# calling the methods and class for male object
print()
m.classH('Human class')
print()
m.classM('male class')
print()
# calling the methods and class for female object
f.classH('human class')
print()
f.classF('female class')
print()

# calling the abstract method
m.gender()
print()
f.gender()
print()

# calling the instance method of male object
m.showH('harry')
print()
m.showM('hriom')
print()
# calling the instance method of female object
f.showH('hello')
print()
f.showF('hii')

# calling the staticS method of male object
m.statH('static method of human class')
print()
m.statM('static methof of male class')
print()

# in the static class we can use constructor variable and can call instance method too

# calling the staticS method of female object
f.statH('hahhaha')
print()
f.statF('hihih')
