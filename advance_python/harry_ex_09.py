

from threading import currentThread, RLock, Lock, Thread

'''
class Bus:
    def __init__(self, avl_st):
        self.avialable_seat = avl_st
        self.l = RLock()  # initialing the Rlock
        print(self.l)  # here it is in unlocked stage

    def reserve(self, req_seat):
        # her it is in locked stage for the thread, we are locking the thread
        self.l.acquire()
        # we have to relase as much time we acquire the thread
        print('available seat', self.avialable_seat)
        if(self.avialable_seat >= req_seat):
            usr_name = currentThread().name
            print(f"{req_seat} seat is alloted for {usr_name}")
            self.avialable_seat -= req_seat
            print(self.l)  # here also the thread is in locked stage
        else:
            print("no seats are available")
        self.l.release()  # here we are releasing or unlocking the thhread
        print(self.l)  # here it is in unlocked stage


b = Bus(2)
pas1 = Thread(target=b.reserve, args=(1,), name='harry')
pas2 = Thread(target=b.reserve, args=(1,), name='hariom')
pas3 = Thread(target=b.reserve, args=(1,), name='mohak')
pas1.start()
pas2.start()
pas3.start()

'''


class Train:
    def __init__(self, avl_seat):
        self.seat_available = avl_seat
        self.rlock = RLock()
        print()

    def reservation(self, tic_req):
        self.rlock.acquire()
        print(self.rlock)
        print("available ticktes", self.seat_available)
        if(self.seat_available >= tic_req):
            usr_name = currentThread().name
            print(f"{tic_req} is booked for {usr_name}\n")
            self.seat_available -= tic_req
        else:

            usr_name = currentThread().name
            print(f"sorry mr.{usr_name}, we have only", self.seat_available,
                  " seats avialable and you have demanded for ", tic_req, " seats . we cant book your tickets\n")

        self.rlock.release()
        print(self.rlock, '\n')


total_seat = int(input("Total seats?:"))
usr1 = input("Enter your name:")
seat_for_usr1 = int(input("Enter how many seats  you want: "))
usr2 = input("Enter your name:")
seat_for_usr2 = int(input("Enter how many seats  you want: "))
usr3 = input("Enter your name:")
seat_for_usr3 = int(input("Enter how many seats  you want: "))

t = Train(total_seat)
pas1 = Thread(target=t.reservation, args=(seat_for_usr1,), name=usr1)
pas2 = Thread(target=t.reservation, args=(seat_for_usr2,), name=usr2)
pas3 = Thread(target=t.reservation, args=(seat_for_usr3,), name=usr3)

pas1.start()
pas2.start()
pas3.start()
pas1.join()
pas2.join()
pas3.join()
print("Thanks for using this ticket booking system")
