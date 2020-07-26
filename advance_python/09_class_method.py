# class method
# class methods are the methods which act upon the class variables or static variable of the class
# decorator @classmethod need to write above the class method
# by default the first parameter of the class method is cls which referes the current class itself

# class decorator without parameter
class Mobile:
    @classmethod
    def show_model(cls):  # class method without parameter
        print("Nokia")


nokia = Mobile()
nokia.show_model()  # calling the class method by object without parameter
Mobile.show_model()  # calling the class method by class without parameter


# class decorator with parameter
class Mobile:
    fp = 'yes'  # class variable

    @classmethod
    def show_model(cls, r):  # class method with parameter
        cls.ram = r
        print("fingerprint:", cls.fp, "ram:", r)


nokia = Mobile()
nokia.show_model('8')  # calling the class method by object with parameter
Mobile.show_model(16)  # calling the class method by class with parameter

print(Mobile.fp)  # accessing the class variable
print(nokia.fp)
