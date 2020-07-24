# constructor
# python supports a special type of method called constructor for initializing the instance variable of class
# a class constructor ,if defined is called whenever a program creates an object of that class.
# a contructor is called only once at the time of creating an instance object
# if two object instances are created for a class , the constructor will be called once for each instance.


# construtor without parameter
'''
class Mobile():
    def __init__(self):
        self.model = 'nokia ka phone'


# creating an object
nokia = Mobile()
print(nokia.model)

'''
# construtor with parameter

'''
class Mobile():
    def __init__(self, p):
        self.model = 'nokia ka phone'
        self.price = p


# creating an object
nokia = Mobile(12000)  # paassing an argument
print(nokia.model)
print(nokia.price)

'''
'''
# construtor with many parameter


class Mobile():
    def __init__(self, p, v=100):
        self.model = 'nokia ka phone'
        self.company = p
        self.value = v


# creating an object
nokia = Mobile('nokia', 110)  # paassing an argument
# here we have passed actual argument, if in the formal argument has default value, it will be replaced by this argument
# we didn't pass the actual argument , the formal agrument will work with its default value
print(nokia.model)
print(nokia.company)
print(nokia.value)

'''
# checking that when constructor call

'''
class Mobile():
    def __init__(self):
        print("Mobile Constructor is called")


obj_cons = Mobile()  # creating an object of class cons
# constructor calls with the creation of object

'''

'''
# constructor without parameter
class Mobile:
    def __init__(self):
        print("Constructor is called here")
        self.model = 'nokia ka phone'

    def show_model(self):
        print("model: ", self.model)


phone = Mobile()  # createated object
phone.show_model()
'''


'''
# construct with parameter

class Mobile:
    def __init__(self, model_1, price_1=20000):
        print("Constructor is called here")
        self.model = model_1
        self.price = price_1

    def show_model(self, com):
        company = com
        print("model:", self.model, "Price:", self.price, "company:", com)


phone = Mobile('nokia 6.1+')  # createated object
phone.show_model('nokia')

# here this is constructor with parameter
# while making the object we have  not passed one argument for the price_1--> it has been taken its default value. if we give its value at actual argument then the default value will be replaced and the new value will be printed on the screen.

'''
