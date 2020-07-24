# each time when we create an object if a class, a copy of each variable deined in the class is created.
# on modifying in any variable will not affect on other, becuase  both have own memory location.


# class Mobile:
#     def __init__(self):
#         self.model = 'nokia 6.1+'

#     def show_model(self):
#         print("Model:", self.model)


# creating objects for this class and cheking their address and mofying its variables

# all the objects will have different memory locations
'''
nokia = Mobile()
print(id(nokia))
print()
samsung = Mobile()
print(id(samsung))
print()

iphone = Mobile()
print(id(iphone))
print()
'''
# harry = Mobile()  # creating an object harry of class mobile
# harry.show_model()  # calling method of object harry

# self has the adress of object harry which is created by mobile

'''
class Mobile:
    def __init__(self):
        self.model = 'Nokia 6.1'

    def show_model(self, p):
        price = p  # local variable
        print("model: ", self.model)


nokia = Mobile()  # here we are making an object for the class mobile
nokia.show_model()  # here we are calling the method
print(nokia.model)  # here we are accessing directly the variable value
a = nokia.model  # here we are storing the variable value into a variable
print(a)  # here we are printing the stored value
'''


# passing a local variable or passing an argument to the method

# class Mobile:
#     def __init__(self, a):
#         self.model = a

#     def show_model(self, a):
#         price = a  # local variable
#         print("model: ", self.model, "price: ", a)
# here both parameter are named as a but both have their own scope and there is no connection between thsese two


# creating an object and passing the argument for model variable
# print("before modification the values are")
# nokia = Mobile('nokia 6.1 plus')
# nokia.show_model(11000)  # passing the argument for show_model method
# print()
# # updating the value
# print("after modification the values are")
# nokia.model = 'nokia 9'
# nokia.show_model(5312324)


# checking ids of the multiobjects of same class

class Mobile:
    def __init__(self, a):
        self.model = a

    def show_model(self, p):
        price = p
        print("model: ", self.model, " price: ", p)


print("Before modification")
nokia = Mobile("nokia 6.1+")
nokia.show_model(1134)
print("id of this object is", id(nokia))
print()

samsung = Mobile('samsung j2 prime')
samsung.show_model(22321)
print("id of this object is", id(samsung))
print()

iphone = Mobile('iphone 11 max pro')
iphone.show_model(98763)
print("id of this object is", id(iphone))
print()


# modifying the object
print("After modification")

nokia.model = 'nokia 5.1'
samsung.show_model = 346433
iphone.model = 'iphone 7'

print(nokia.model)
print(samsung.show_model)
print(iphone.model)
