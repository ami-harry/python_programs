# method overloading
# when more than one method with the same name is different in the same class, it is known method overloading

# in python, if a method is written such that it can perform more than one taks,it is called method overloading.


'''

class Myclass:
    def sum(self, a):
        print("first sum method", a)

    def sum(self):
        print("second sum method")


obj = Myclass()
obj.sum(10)
obj.sum()

# it will run with an eror
#     obj.sum(10)
# TypeError: sum() takes 1 positional argument but 2 were given

'''


class Myclass:
    def sum(self, a=None, b=None, c=None):
        if a != None and b != None and c != None:
            print(a+b+c)
        elif a != None and b != None:
            print(a+b)
        else:
            print('enter atleaast 2 parameter')


obj = Myclass()
obj.sum(3)
