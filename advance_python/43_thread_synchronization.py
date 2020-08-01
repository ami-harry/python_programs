# thread synchrnization
# many threads trying to access the same object can lead to problems like making data inconsistent or getting unexcpected output. so when a thread is already accessing an object. preveneting any other thread accessing the same object is called thread synchronization
# the object on which the threads are synchronized is called synchronized object or mutually execlusive lock(mutex)
# thred sunchronization is recommended when multiple threads are acting on the same object simultaneously.
# there are following technique to do thread synchronization
# using locks
# using Rlock(re extract lock)
# using semaphones

# locks
# locks are typically used to synchronize access to a shared resource. locak canhn be used to lock tge object in which the thread is acting. a lock has only two states locked and unlocked. it is created in the unlocked state

# acquire()
# this method is used to change the state to locked and returns immediately. when the state is locked aquire() blocks untill a call to release() in another thread changes it to unlock, then the acquire() call resets it to locked and returns
# syntax
# acquire(blocking=True, timeout=-1)
# True-> it blocks untill the lock is unlocked then set it to locked and return True
# False--> it does not block. if a call with blocking set to True would block. return False immediately; otherwise , set the lock to locked and return True
# timeout--> When invokjed with the floating point argument set to a positive value. block for  at most the number of seconds specified by timeout and as long as the lock can not acquire . a timeout argument of 1-specifies an unbounded wait. it is forbidded to specify a timeout when blocking is False.
# The return value is True if the lock is acquired sucessfully, False if not(for example if the timeout expired)

# release()
# this method is used to release a lock. this can be called from any thread, not only the thread which has acquire the lock
# when the lock is locked, reset it unlocked and return. if any other threads are blocked waiting for the lock to become unlocked allows exacty one of them to proceed.
# when invoked on an unlocked lock, a RuntimeError is raise
# there is no return Value
# syntax --> release()


from threading import Thread, currentThread, Lock


class Flight:
    def __init__(self, avl_seat):
        self.aviable_seat = avl_seat
        self.l = Lock()

    def reserve(self, need_seat):
        # by default blocking is True and timeout is -1
        self.l.acquire()
        print("available seat:", self.aviable_seat)
        if(self.aviable_seat >= need_seat):
            user_name = currentThread().name
            print(f"{need_seat} is booked to {user_name}")
            self.aviable_seat -= need_seat
        else:
            print('no seat is available')
        self.l.release()


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
