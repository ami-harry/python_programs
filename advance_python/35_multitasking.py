# multitasking
# executing multiple task at the same time
# types of multitasking
# a. process based multitasking
# b. Thread based multitasking


# a.  process based multitasking
# executing multiple task at the same time where each task is seperate indpendent program(process), is called process based multitasking. it is suitable for operating system level.


# b. Thread based multitasking
# executing multiple task at the same time where each task is seperate indpenedent part of the same program (process) is called Thread based multitasking and eacgh independent part is called. it is suitable for program level.

# Thread
# Thread is a seperate flow of execution. Every thread has a task.

# Multithreading
# using multiple thread in program

# the main important application areas of multithreading area
# >-->> multimedia graphic
# >-->> animations
# >-->> video games
# >-->> web servers
# >-->> application servers


# main thread
# when we start python program, one thread begins running immediately, which is called main thread of that program created by PVM.

# the main thread is created automatically when your program is created/started

'''
import threading
t = threading.currentThread().getName()
print("hello harry")
print(t)

'''

# creating a Thread

# Thread class of threading module is used to create threads.
# to create our own thread we need to create an object of Thread class


# following are the way of creating thread
# creating a thread without using a class
# creating a thread by creating a child class to Thread class
# creatind a thread without child class to Thread class


# creating a thread without using a class
# from threading import Thread
# Thread_object=Thread(target=function_name,args=(arg1,arg2))
# Thread_object--> it represents our thread
# target--> it represents the function on which the thread will act
# args--> it represents a tuple of argument which are passed to the function


# ex--> t=Thread(target=disp,args(10,20))


# how to start Thread
# once a Thread is created it should be strated by calling start() method


'''
from threading import Thread

# creating the function on which the thread will perform its action


def disp(a, b):
    """this function will passed into thread as its parameter"""  # """this is doct string for the function"""

    print("thread is running", a, b)


# creating the thread and passing its argument
t = Thread(target=disp, args=(10, 20))
t.start()  # starting the Thread
print(disp.__doc__)  # printing the definition of the function

'''
'''



from threading import Thread
def disp():
    print("Thread is running")


for i in range(5):
    t = Thread(target=disp)
    t.start()

'''
'''

from threading import Thread

def disp():
    print("Child Thread is running")
    print("Child Thread is running")


for i in range(5):
    t = Thread(target=disp)
    t.start()

for i in range(5):
    print("Main thread")
'''
# we cant predict that which thread will run first and which will the last
# infact we cant determine the order of threads running
