# accessor method
# this method is used to access or read data of the variable. this method do not modify the data in the variable. this is also called as getter metho

# ex -->
# def get_company(self):
# def get_model(self):
# def get_price(self):
# def get_id(self):
#


# example


class Mobile:
    def __init__(self):
        self.model = 'nokia 6.1+'

    def get_model(self):
        return self.model
        # this function returns the model
# we have to store the returned value and can print to see the output


nokia = Mobile()
ret = nokia.get_model()
print(ret)
print()

# mutator method
# this method is used to access or read or modify the data of the variables. this method modify the data in the variable. this is also called as setter method


# def set_name(self):
# def set_price(self):
# def set_model(self):
# def set_id(self):

# without parameter

class Mobile:
    def __init__(self):
        self.model = 'nokia 6.1+'
        print("Before set_model")
        print("model:", self.model)

    def set_model(self):
        # here we are setting the model or modifying the data of the instance variable
        self.model = 'nokia 5.1+'
        print("after set_model")
        print("model:", self.model)


nokia = Mobile()
nokia.set_model()

print()


# with parameter
class Mobile:
    def __init__(self):
        self.model = 'nokia 6.1+'
        print("Before set_model")
        print("model:", self.model)

    def set_model(self, m):
        # here we are setting the model or modifying the data of the instance variable
        self.model = m
        print("after set_model")
        print("model:", self.model)


nokia = Mobile()
# here we are passing the argument so set method will make changes
nokia.set_model('nokia 9')
