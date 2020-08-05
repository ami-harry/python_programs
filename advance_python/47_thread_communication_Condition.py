# condition for thread communication

# condition class is used to improve speed pf communcation between Threads. the condition class object is called condition value

# a condition variable is always associated with some kind of lock, this can be passed in or one will be created by default. passing one is useful when several condition vriables must share the same lock. the lock is paart of the condition object; you dont have to track it seperately
# a condition is a more advanced version of the event object

# create condition object
# from threading import Condtion
# cv=Condition

# Condition method
# notify(n=1)---> this method is used to immediately wake up one thread waiting on the condition. where n is the numbers of thread need to wake up

# notify_all()---> this method is used to wake up all threads waiting on the condition

# wait(timeout=None)---> this method wait until notified or until a timeout occurs. if the calling thread has not acquired the lock. when this method is called , a RuntimeError is eaised . wait terminated when invokes notify() method or notify_all() method. the return value is True unless a given timeout expired, in which case it is False


from threading import Thread, Condition
from time import sleep


lst = []


def production():
    cv.acquire()  # locking the thread
    for i in range(1, 6):
        lst.append(i)
        sleep(2)
        print("produced item no ", i)
    cv.notify()  # notifying one thread, for all we will use notify_all() , we can pass n as no of threads we want to notify
    cv.release()  # releasing the acquired lock


def consume():
    cv.acquire()  # locking the thread for this function
    cv.wait(timeout=0)
    # for i in lst: #printing the list
    # print(i)
    print()
    print("produced items are")
    print(lst)
    cv.release()


cv = Condition()
th1 = Thread(target=production)
th2 = Thread(target=consume)

th1.start()
th2.start()
