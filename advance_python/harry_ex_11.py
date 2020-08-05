# thread condition
# on user input


from threading import Thread, Condition
from time import sleep

lst = []  # empty list to store the data
no_of_item = int(input("Enter how many item you want to produce:"))


def production():
    cv.acquire()
    for i in range(1, no_of_item+1):
        lst.append(i)
        print("Item no", i, "produced")
        sleep(2)
    cv.notify()
    cv.release()


def consume():
    cv.acquire()
    cv.wait(timeout=0)
    cv.release()
    print('Produced items are')
    print(lst)


cv = Condition()
th1 = Thread(target=production)
th2 = Thread(target=consume)
th1.start()
th2.start()
