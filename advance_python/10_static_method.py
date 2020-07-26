# static method
# static methods are used when some processing is related to the class but does not need the class or its instances to perform any work.
# we use static method when we want to pass values from outside and perform some action in the method


# decorator @staticmethod need to write above the static method

# static method without parameter

class Mobile:
    @staticmethod
    def show_model():
        print('nokia 6.1+')


nokia = Mobile()
Mobile.show_model()  # calling the static method without argument

# static method with parameter


class Mobile:
    fp = 'yes'  # class variable

    @staticmethod
    def show_model(m, p):
        model = m
        price = p
        print("Model:", m)
        print('price:', p)
        print('fingerprint:', Mobile.fp)  # accessing the class variable


nokia = Mobile()
Mobile.show_model('nokia 6.1+', 12000)  # calling static method with parameter
