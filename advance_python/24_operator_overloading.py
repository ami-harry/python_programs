# operator overloading

# for every operator a method is written and that executes behing the scenes and the action performs
# for int, str, float methods are defined and we can add them
# but for adding classes we have to make our own method which will take two ojbects as argument and will add them..

# these are some methods defined
# int.__add__(self, other) here int is class and add is its method
# int.__mul__(self,other) here int is class and mul is its method
# str.__add____(self,other) here str is class and add is its method

# like these we also have to make our own methods which will add two object

# print(10+20)
# print(int.__add__(10, 20))
# print("hello "+"harry")
# print(str.__add__('hello ', 'harry'))
# print(10*15)
# print(int.__mul__(10, 15))


class A:
    def __init__(self, x):
        self.value = x

    def __add__(self, other):  # method to add objects
        return self.value + other.value


class B:
    def __init__(self, x):
        self.value = x


a = A(45)
b = B(45)

print(a+b)  # passing two objects to add
