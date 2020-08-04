# thread communication
# two or more threads communicate with each other
# 1. event
# 2. condition
# 3. queue


# event
# this is one of the simplest mechanism for communication between threads ; one thread signals an event and other wait for it
# an event object manages an internal flag that can be set to True with the set() method and reset to False with the clear() method. the wait() method blocks until the flag is True
# the flag is initially True
# create event object
# from threading import event
# e=event()


# event methods
# set()--> it sets the initial flag to True. all threads waiting for it becomes True are awakend. Threads are call wait() once the flag is True will not block at all
# clear()--> it resets the initial flag to False. subsquently threads calling wait() will block until set() is called to set the internal flag to True again
# is_set()---> it returns True if and only if the internal flag is True
# wait(timeout=None)--> it blocks until the flag us True.
# if the initial flag is True or entry, return immediately , otherwise , block until another threads call set() to set the flag to True or until the optional timeout
# when the timeout argument is present and not none, it should be a floating point nuumber specifying a timeout for the seconds(or fraction there of)
# this method returns True if only if the internal flag has been set to True, either before the eait or call or after the wait starts, so it will always return True except if a timeout is given and the operation times out

from threading import Event, Thread
from time import sleep


def signal_light():
    sleep(2)  # it will hold the screen to print the output
    e.set()  # here the condition is True , it will print becuase the condition is True
    print('green light signal')
    sleep(5)  # it will print in 5 seconds
    print('red light signal')
    e.clear()  # here the conditions will get False


def traffic():
    e.wait()
    while e.isSet():  # here it will run when the condition is true
        print("You can go!")
        sleep(.5)  # it will print every output in .3 secondsI
    print('program end')


e = Event()

t1 = Thread(target=signal_light)
t2 = Thread(target=traffic)

t1.start()
t2.start()
