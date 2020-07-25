# types of variables

# instance variable
# class varibale/static variable

# instance variable
# instance variable are the variables whose seperate copy is created in every object. instance variables are defined and initialized using a constructor with self parameter


'''
class Mobile:
    def __init__(self):
        self.model = 'nokia 6.1+'  # instance variable

    def show_model(self):
        print("Model:", self.model)


nokia = Mobile()
nokia.show_model() #accessing the instance variable 

'''

'''
# accessing the instance variable
# with instance method


class Mobile:
    def __init__(self):
        self.model = 'nokia 6.1+'  # instance variable

    def show_model(self):  # instance method
        print(self.model)  # accessing the instance variable


nokia = Mobile()
nokia.show_model()

'''

'''

# outside class:
class Mobile:
    def __init__(self):
        self.model = 'nokia 6.1+'  # instance variable

    def show_model(self):  # instance method
        print(self.model)  # accessing the instance variable


nokia = Mobile()
# accessing the instance variable from outiside the class. here we can print and modify
nokia.model
# accessing the instance method from outiside the class. here we can print and modify
nokia.show_model()

'''


# instance variable
# instance variable are the variable whose seperate copy is created in every object. if we modify the copy of instance variable in an instance, it will no affect all the copies in the other instance


class Mobile:
    def __init__(self):
        self.model = 'nokia 6.1+'  # instance variable

    def show_model(self):  # instance method
        print(self.model)  # accessing the instance variable


nokia = Mobile()
samsung = Mobile()
lenovo = Mobile()

# the original values are
print("The original values are")
print(nokia.model)
print(samsung.model)
print(lenovo.model)
print()
# modifying the values
print("Ater modification in object variable:")
lenovo.model = 'lenovo k8 note'
samsung.model = 'samsung j7 prime'
print(nokia.model)
print(samsung.model)
print(lenovo.model)
print()
