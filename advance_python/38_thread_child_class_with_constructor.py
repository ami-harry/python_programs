from threading import *


class Mythread(Thread):
    def __init__(self, a):
        Thread.__init__(self)  # calling the parent class constructor
        print("child class constructir", a)

    def run(self):
        for i in range(5):
            print("This is pass method")

    def showM(self):
        for i in range(5):
            print("This is instance method")


# creating its object and passing the parameter and the constructow rill be called
'''
mt = Mythread(10)
mt.start()
mt.run()
mt.showM()
for i in range(5):
    print("main thread")
# in this case the output will be unordered
#  to make them an arrange format as output we have to use join method()
'''

mt = Mythread(10)
mt.start()
mt.join()
mt.run()
mt.showM()
for i in range(5):
    print("main thread")


# we can use classmethod,static method, instance method, abstract method, interface and all in this way