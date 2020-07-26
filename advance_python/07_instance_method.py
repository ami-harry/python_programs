# types of method
# instance method
#        accessor method
#        mutator method
#
# class method
# static method

# instance method
# instance methods are the methods which act upon the instance variable of the clas. instance method need to know the memory address of the instance which is provied through self variable by default as first parameter for the instance method

# syntax-->
# def method_name(self):
#     function body
# instance method without parameter


#
# def method_name(self,arg1,agr2..):
#     function body
# instance method with parameter

'''
# instance method without parameter
# calling instance method without parameter
# instance methods are bound to object of the class so we call instance method with object name


class Mobile:
    def __init__(self):
        self.model = 'nokia 6.1+'

    def show_model(self):  # instance method without formal argument
        print("model:", self.model)


nokia = Mobile()
nokia.show_model()  # calling the instance method without actual argument

lenovo = Mobile()
lenovo.show_model()


# instance method with parameter

class Mobile:
    def __init__(self, m):  # here we are also passing an argumet
        self.model = m

    def show_model(self, p):  # instance method with formal argument as p
        # instance variable
        self.price = p  # or price=p (p is argument)
        print("model:", self.model, "price:", self.price)


nokia = Mobile('nokia 6.1+')
nokia.show_model(12344)  # calling the instance method with actual argument
lenovo = Mobile('lenovo k8 note')
lenovo.show_model(41232)

'''