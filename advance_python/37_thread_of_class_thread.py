# Creating a thread by creating a child class to Thread class

#  we can create our own thread class by inheriting Thread class from the threading module
from threading import Thread
'''


class ChildClasName(Thread):
    statementsclass MyThread(Thread):
    def run(self):
        for i in range(10):
            print("run method")


ob = MyThread()
print(ob.name)
ob.start()
for i in range(5):
    print("main thread")


thread_object = ChildClasName()
'''
'''


from threading import Thread


class MyThread(Thread):
    pass


ob = MyThread()
print(ob.name)

'''


# Thread class method
# start() --> once a thred is created it should be started by calling start()
# run() --> every thread will run this method when thread is started. we can override this method and write our own code as body of this method. a thread will terminate automatically when it  comes out of run() method
# join() --> This method is used to wait till the method completly executes the run() method

'''
class MyThread(Thread):
    def run(self):
        print("run method")


ob = MyThread()
print(ob.name)
ob.start()
print("main thread")

'''
'''


class MyThread(Thread):
    def run(self):
        for i in range(10):
            print("run method")


ob = MyThread()
print(ob.name)
ob.start()
for i in range(5):
    print("main thread")

# we can manage the flow of execution of the Threads. by using join method

'''


class MyThread(Thread):
    def run(self):
        for i in range(10):
            print("run method")


ob = MyThread()
print(ob.name)
ob.start()
ob.join()  # firstly the run method will execute then main will execute
for i in range(5):
    print("main thread")
