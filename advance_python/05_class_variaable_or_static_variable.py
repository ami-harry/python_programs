# class variable
# class variable are the variable whose single copy is available to all the instance of the class. if we modify the copy of class variable in an instance, it will effect all the copies in the other variable.


'''
class Mobile:
    fp = 'yes'  # this is class variable

    def __init__(self):
        self.model = 'Nokia 6.1+'  # instance variable

    def show_model(self):  # instance method
        # accessing instance variable, we can modity it here also
        print(self.model)


nokia = Mobile()
'''

'''
# accessing class method

# with class method
# to access the class variable , we need class method with cls as first parameter then we can acceess class variable using cls.var_name

class Mobile:
    fp = 'yes'  # this is class variable

    def __init__(self):
        self.model = 'Nokia 6.1+'  # instance variable

    def show_model(self):  # instance method
        # accessing instance variable, we can modity it here also
        print(self.model)

    @classmethod
    def is_fp(cls):  # class method
        cls.fp  # accessing the class variable ., we can modify the variable here


nokia = Mobile()

'''

'''
# outside class


class Mobile:
    fp = 'yes'  # this is class variable

    def __init__(self):
        self.model = 'Nokia 6.1+'  # instance variable

    def show_model(self):  # instance method
        # accessing instance variable, we can modity it here also
        print(self.model)

    @classmethod
    def is_fp(cls):  # class method
        cls.fp  # accessing the class variable ., we can modify the variable here


nokia = Mobile()
Mobile.fp  # accessing class variable outside the class, using class_name.var_name

'''


'''
# class variable:
# class variable are the variable whose single copy is available to all the instance of the class, if we modify the copy of variable in an instance, it will affect in all the copies of the other instance


class Mobile:
    fp = 'yes'  # this is class variable

    @classmethod
    def is_fp(cls):  # class method
        # accessing the class variable ., we can modify the variable here
        print("fingerprint:", cls.fp)


nokia = Mobile()
samsung = Mobile()
lenovo = Mobile()
print('accessing class variable')
print(Mobile.fp)

# modifying class variable, it will affect on all objects
Mobile.fp = 'no'

print(Mobile.fp)

# it will print the modifed value

# or accessing the class variable using class method ouside the class

Mobile.is_fp()
# it will print the modifed value

'''


# class variable or static variable with class method


class Mobile:
    fp = 'yes'  # this is class variable

    def __init__(self):
        self.model = 'Nokia 6.1+'  # instance variable

    def show_model(self):  # instance method
        # accessing instance variable, we can modity it here also
        print(self.model)

    @classmethod
    def is_fp(cls):  # class method
        # accessing the class variable ., we can modify the variable here
        print("fingerprint:", cls.fp)


nokia = Mobile()
samsung = Mobile()
lenovo = Mobile()

print("This is instance variable, modifing on this variable will not affect on all the instance")
nokia.show_model()
samsung.show_model()
lenovo.show_model()
# modifying instance variable
nokia.model = 'this is changed manually to nokia 5.1'
lenovo.model = 'this is changed manually lenovo k8 note'
print()
print("after modification the instance variable are ")
nokia.show_model()
samsung.show_model()
lenovo.show_model()

print()
# accessing class method using class name
print("accessing lass method")
Mobile.is_fp()
print()

print("the original class variable were")
print('Nokia', Mobile.fp)
print('samsung', Mobile.fp)
print('lenovo', Mobile.fp)
print()
# modifying class variable , it will effect on all objects
print("after modification in ove variable")
Mobile.fp = 'no'
print('Nokia', Mobile.fp)
print('samsung', Mobile.fp)
print('lenovo', Mobile.fp)

print()
