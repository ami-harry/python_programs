# make own methods to do arithimatic operations with objects
# take input from user and five output

class A:
    def __init__(self, val1):
        self.value = val1

    def __add__(self, arg1):
        return self.value + arg1.value

    def __mul__(self, arg1):
        return self.value * arg1.value

    def __sub__(self, arg1):
        return self.value - arg1.value


class B:
    def __init__(self, val1):
        self.value = val1
        super().__init__()


num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))


a = A(num1)
b = B(num2)

print(a+b)
print(a-b)
print(a*b)
