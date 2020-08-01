# program that creates race condition

# race condition
# race condition is a situation that occurs when threads are acting in an unexpected sequence , this leading to unreliable output

# this can be eliminated using thread synchronization


from threading import Thread, currentThread


class Flight:
    def __init__(self, avl_seat):
        self.aviable_seat = avl_seat

    def reserve(self, need_seat):
        print("available seat:", self.aviable_seat)
        if(self.aviable_seat >= need_seat):
            user_name = currentThread().name
            print(f"{need_seat} is booked to {user_name}")
            self.aviable_seat -= need_seat
        else:
            print('no seat is available')


f = Flight(1)
t1 = Thread(target=f.reserve, args=(1,), name='harry')
t2 = Thread(target=f.reserve, args=(1,), name='hariom')
t1.start()
t2.start()
