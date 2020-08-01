# creating race condition problem using multiple thread:

from threading import Thread, currentThread


class Bus:
    def __init__(self, seat):
        self.avl_seat = seat

    def reserve(self, req_seat):
        print('total seat available is', self.avl_seat)
        if(self.avl_seat >= req_seat):
            usr_name = currentThread().name
            print(f"{req_seat} is booked for {usr_name}")
            self.avl_seat -= req_seat
        else:
            print('no seat available')


usr1 = input("Enter your name: ")
need_seat1 = int(input("Enter how many seat you want: "))
usr2 = input("Enter your name: ")
need_seat2 = int(input("Enter how many seat you want: "))

b = Bus(5)
t1 = Thread(target=b.reserve, args=(need_seat1,), name=usr1)
t2 = Thread(target=b.reserve, args=(need_seat2,), name=usr2)
t1.start()
t2.start()

# this will show an error, it will give unexpected output
