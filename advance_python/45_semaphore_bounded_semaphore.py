# semaphore
# this is one of the oldest synchronization primitives in the history of computer science; invented by the early Dutch coputer scientist Engineer W. Dijkstra
# a semaphore manages an internal counter which is decremented by each acquire() call and incremented by each release() call.
# the counter can never go below zero; when acquire() finds that it is zero, it blocks, waiting untill some other threads call release().
# it's usually better to use the BoundedSemaphore class, which considers it to be an error to call relase more ofter th you've called acquire
from threading import *


class Bus:
    def __init__(self, avl):
        self.seat_avl = avl
        # by using semaphre we can aquire and release as much times as we want
        # self.l = Semaphore(sl)
        self.l = BoundedSemaphore(sl)
        # it will print the limit incr/decr status
        print("total threads", self.l._value)

    def book(self, req_tic):
        self.l.acquire()  # here we are locking the thread
        # it will print the limit incr/decr status
        print("working threads", self.l._value)
        print("Total seat available:", self.seat_avl)
        if(self.seat_avl >= req_tic):
            usr_name = current_thread().name
            print(f'{req_tic} tickets booked for {usr_name}')
            self.seat_avl -= req_tic
        else:
            print("no tickets available")
        self.l.release()  # here we can aquire and release many times there is no bound


sl = int(input("Enter semaphore limit: "))
limit = int(input("Enter total seats: "))
usr_1 = input("Enter your name: ")
tic_usr1 = int(input("How many seats you want: "))
usr_2 = input("Enter your name: ")
tic_usr2 = int(input("How many seats you want: "))
usr_3 = input("Enter your name: ")
tic_usr3 = int(input("How many seats you want: "))
# usr_4 = input("Enter your name: ")
# tic_usr4 = int(input("How many seats you want: "))
# usr_5 = input("Enter your name: ")
# tic_usr5 = int(input("How many seats you want: "))


b = Bus(limit)
pas1 = Thread(target=b.book, args=(tic_usr1,), name=usr_1)
pas2 = Thread(target=b.book, args=(tic_usr2,), name=usr_2)
pas3 = Thread(target=b.book, args=(tic_usr3,), name=usr_3)
# pas4 = Thread(target=b.book, args=(tic_usr4,), name=usr_4)
# pas5 = Thread(target=b.book, args=(tic_usr5,), name=usr_5)

pas1.start()
pas2.start()
pas3.start()
# pas4.start()
# pas5.start()
print("thanks for using ticket booking system using semaphore")

# it will give confusing output
# which thread is entering and exiting will confues the output


# boundedsemaphore will give the correct ouput but will lead to deadlock
