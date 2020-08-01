#  Multitasking_using_Multiple_Thread
# when multiple tasks are executed at a time, then it is called multi-tasking. for this purpose we need more than one thread and when we use more than one threa is called multi-thread


from threading import Thread


class Hotel:
    def __init__(self, t):
        self.take_order = t

    def serve_order(self):
        for i in range(1, 6):
            print(self.take_order, i)


h1 = Hotel("take order from table ")
h2 = Hotel("serve order to table ")
t1 = Thread(target=h1.serve_order)
t2 = Thread(target=h2.serve_order)
t1.start()
t2.start()

# in this output we will see error that somewhere cases we are serving the food before taking the order
# this is an error called race error
