# Queue
# The Queue class of queue module is useful to create a queue that holds the data produced by the producer
# the data can be taken from the queue and utilized by the consumer
# we need not to use locks since queues aree threads safe


# create queue object
# from queue import Queue
# q = Queue()


# Queue method
# put()--> This method is used by producer to insert items into the queue
# syntaz--> queue_object.put(item)
# q.put(i)

# get()--> this method is used by consumer to retrieve items from the queue
# syntaz--> producer_object.queue_onject.get(item)
# ex-> p.q.get(i)

# empty()--> this method returns True if queue is empty else False
# ex-->q.empty()

# full()--> this method returns True if queue is full else False
# ex -> q.full()


from threading import Thread
from queue import Queue
from time import sleep


class Producer:
    def __init__(self):
        self.q = Queue()

    def produce(self):
        for i in range(1, 6):
            print("data procduced", i)
            self.q.put(i)
            sleep(2)
            print()


class Consumer:
    def __init__(self, pro):
        self.prod = pro

    def consume(self):
        for i in range(1, 6):
            print('item receiver', self.prod.q.get(i))


p = Producer()
q = Consumer(p)


t1 = Thread(target=p.produce)
t2 = Thread(target=q.consume)
t1.start()
t2.start()
