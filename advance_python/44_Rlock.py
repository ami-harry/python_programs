from threading import Thread, currentThread, Lock, RLock


class Flight:
    def __init__(self, avl_seat):
        self.aviable_seat = avl_seat
        self.l = RLock()
        print(self.l)  # here it is show the ublocking

    def reserve(self, need_seat):
        # by default blocking is True and timeout is -1
        self.l.acquire()
        print(self.l)  # here it is locked for the thread
        print("available seat:", self.aviable_seat)
        if(self.aviable_seat >= need_seat):
            print()
            print(self.l)  # here also it is already in locked stage
            print()
            user_name = currentThread().name
            print(f"{need_seat} is seat booked to {user_name}")
            self.aviable_seat -= need_seat
            print()
            print(self.l)  # here is also in locked stage
            print()
        else:
            print('no seat is available')
        self.l.release()
        print(self.l)  # here it will release it


f = Flight(2)
t1 = Thread(target=f.reserve, args=(1,), name='harry')
t2 = Thread(target=f.reserve, args=(1,), name='hariom')
t3 = Thread(target=f.reserve, args=(1,), name='hk')
t1.start()
print()
t2.start()
print()
t3.start()
print()
t1.join()
print()
t2.join()
print()
t3.join()
print()
print('main thread')
