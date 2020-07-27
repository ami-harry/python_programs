# method overriding
# if we write same method in the both class parent class and child class then the parent class method is not available in child class.
# in this case only child class method is accessible which means child class method is replacing parent class.
# method overriding is used when progrmmer want to modify the existing behaviour of a method
'''
class Add:
    def result(self, a, b):
        print("Addition:", a+b)


class Multi(Add):
    def result(self, a, b):
        print("multiplication:", a*b)


# here both method name is same and only child method will be execute
a = Multi()
a.result(54, 67)

'''
# to use parent method also we have to use super() method

# method overriding with super methdo
# super method is used to call parent class constructor and method from the child class


class Add:
    def result(self, a, b):
        print("addition:", a+b)


class Multi(Add):
    def result(self, a, b):
        print("multiplication:", a*b)
        return super().result(a, b)  # calling parent method using super method


a = Multi()
a.result(10, 20)
