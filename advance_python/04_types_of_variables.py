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
nokia.show_model()

'''
