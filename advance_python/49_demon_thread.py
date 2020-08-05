from threading import currentThread, Thread
from time import sleep
# Daemon Thread
# a daemon thread is a thread which runs continuosly in the background. it provides support to non-daemon threads

# when last non-deamon thread terminates, automatically all daemon threads will be terminated. we are not required to terminte daemon thread seperately.

# create daemon thread
# setDaemon(True) method or daemon=True ,property is used to make a thread as daemon thread

# ex--> t1= Thread(target=disp)
# t1.setDaemon(True) (method) or
# t1.daemon=true  (property)


# method
# setDaemon(True/False)--> this method is used to set a thread as daemon thread. you caan set thread as daemon only before starting the thread which means active thread statusb can not changed as daemon
# if we pass True non_daemon thread will become daemon and if False daemon thread will become non-daemon
# deamon property--> This property is used to check whether a thread is daemon or not. it returns True if thread is daemon else False
# we can also use deamon property to set a thread as daemon thread or vice versa
# isDaemon()--> this method is used to check whether a thread is daemon or not, it returns True if thread is daemon else False

'''

from threading import Thread


def disp():
    print("Daemon Thread")


t1 = Thread(target=disp)
print('before ', t1.isDaemon())
# t1.setDaemon(True) #this is using method
# t1.daemon=True #this is using property
print('after ', t1.isDaemon())
t1.start()  # starting the thread

# if we start the thread and then if we are changing it to the daemon, it will show an error than at runtime we cant change a thread as non-daemon to daemon and as daemon to non-daemon

'''


# default nature of daemon thread
# a. main thread is always non-daemon thread

'''
#       checking the proerty of daemon thread

from threading import currentThread, Thread
mt = currentThread()
print(mt.getName())  # running thread name
print(mt.isDaemon())  # is the running thread is daemon or not
# hence proved the main thread is non-daemon thread

'''

# b. rest of the threads inherits daemon nature from their parent
# b.1   if parent thread is non-daemon then child thread will become non-daemon thread
# b.2   if parent thread is daemon then child thread will become daemon thread

'''


# b.1   if parent thread is non-daemon then child thread will become non-daemon thread
def disp():
    print("Disp function")


mt = currentThread()
print(mt.getName())
print("mt", mt.isDaemon())
t1 = Thread(target=disp)
print('t1:', t1.isDaemon())
# here main thread is the  child of t1 thread so it will also be a non-daemon thread

# b.2   if parent thread is daemon then child thread will become daemon thread


def disp():
    print("Display function")
    t2 = Thread(target=show)
    print("t2:", t2.isDaemon())
    t2.start()


def show():
    print("Show function")


mt = currentThread()
print(mt.getName())
print("mt:", mt.isDaemon())
t1 = Thread(target=disp)
print('t1 before:', t1.isDaemon())
t1.daemon = True
print('t1 after:', t1.isDaemon())
t1.start()
t1.join()

'''
# c. when last non daemon thread terminates, automatically all daemon threads will be terminated , we are not required to terminate daemon thread explicitly


def teacher():
    for i in range(1, 10):
        print("Teaching session", i)
        sleep(1)


t1 = Thread(target=teacher)
t1.daemon = True
t1.start()
sleep(7)
print("Exam finished\n", currentThread().name)
