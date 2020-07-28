# this is module file
# here the methods ,vaariables, functions , classes will be written and these will be access into another file


def sum():
    var1 = int(input("Enter the fist number: "))
    var2 = int(input("Enter second number: "))
    # return "the sum is ", var1+var2
    print("the sum is ", var1+var2)


class Mobile:
    mcv = 'harry'

    def __init__(self):
        print("this is constructor of mobile class")

    def show(self):
        print("this is instance method of mobile class")

    @classmethod
    def clsM(cls):
        print("This is class method of mobile class")
        print("Class variable is ", cls.mcv)

    @staticmethod
    def statM():
        print("this is static method of mobile class")


def mul(a, b):
    print("the multiplication is ", a*b)


def square(a):
    print("the square is ", a*a)


num1 = 10
num2 = 20
