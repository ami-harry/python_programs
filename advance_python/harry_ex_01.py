# taking input in list and passing the list as  the actual of class while making the object
# using super() method  passing the 2 arguments , one in child class and one in parent class

class Father:
    def __init__(self, name):  # parent constructor with one formal parameter
        self.name = name  # parent constructorI variable
        print("parent class constructor is called")

    def show(self):
        print("parent class instance method")
        super().__init__()


class Son(Father):
    def __init__(self, name, roll):  # child constructor with one formal parameter
        super().__init__(name)  # calling the parent constructor  by super() method
        self.roll = roll #this is called
        print("child class constructor is calling")

    def disp(self):
        print("child class instance method")
        print("input name in parent class is ", self.name)
        print("input roll is child class is ", self.roll)


a = []
b = []
size = int(input("Enter the size of the list:"))

for data in range(size):
    print("Enter tha name for items in the list at index no ", data, end='')
    a.append(input(": "))

print("The list items are")
print(a)

size1 = int(input("Enter the size of the list:"))

for data1 in range(size1):
    print("Enter tha roll for items in the list at index no ", data1, end='')
    b.append(int(input(": ")))

print("The list items are")
print(b)

print("creating the object are passing these list as its argument")
# creating object and and passing the lists as argument

s = Son(a, b)
s.disp()  # calling the method
