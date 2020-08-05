
# thread communication
# connecting two threads
# one thread will wait for another to execute then after the second will execute

from threading import Thread, Event
from time import sleep


def light():
    sleep(3)
    e.set()
    print("Green Light on")
    sleep(5)
    print("Red light on")
    e.clear()


def traffic_ctrl():
    e.wait()
    while e.is_set():
        print("You can go...")
        sleep(.25)
    print('program end')


e = Event()
th1 = Thread(target=light)
th2 = Thread(target=traffic_ctrl)
th1.start()
th2.start()
