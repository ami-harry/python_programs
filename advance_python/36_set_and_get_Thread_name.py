# set and get Thread name

# current_thread---> This function returns current thread object
# get_name() --> every thread has  a name by default , to get the name of thread we can use this method
# set_name() --> This method is used to set the name of therad
# name--> this property is used to get or set the name of the thread


from threading import Thread, currentThread

'''
def disp():
    print("child thread name", currentThread())


t = Thread(target=disp)
t.start()

print("Main thread name:", currentThread())
# current_thread will return the by default name of the thread name a unique no, the unique no will change with every execution
'''

'''
# using getName to see the name of thread


def disp():
    print("child thread name", currentThread().getName())


t = Thread(target=disp)
t.start()

print("Main thread name:", currentThread().getName())

'''
'''


# using setName to see the name of thread


def disp():
    print("child thread name", currentThread().getName())
    currentThread().setName('child thread')
    print("child thread name", currentThread().getName())


t = Thread(target=disp)
t.start()

print("Main thread name:", currentThread().getName())
currentThread().setName('harry')
print("Main thread name:", currentThread().getName())

# the order of execution will not be proper, becuase it is multitasking, it is performing many task at the same time, so the output will not be proper

'''
'''

# using name property to see defau;t name of the thread


def disp():
    print("child thread name", currentThread().name)


t = Thread(target=disp)
t.start()

print("Main thread name:", currentThread().name)
# it will return the default name only

'''
'''

# using name property to set the name of thread


def disp():
    print("child thread name", currentThread().name)
    currentThread().name = 'child thread'
    print("child thread name", currentThread().name)


t = Thread(target=disp)
t.start()

print("Main thread name:", currentThread().name)
currentThread().name = 'harry'
print("Main thread name:", currentThread().name)
# we have change the default name of the thread

'''
'''

# using name property without function


def disp():
    pass


t = Thread(target=disp, name='child thread')
print('child thread name:', t.name)
print('child thread name:', t.getName())
# both will give same output
t.start()
# print("Main thread name:", currentThread().name)
# currentThread().name = 'harry'
# print("Main thread name:", currentThread().name)
# # we have change the default name of the thread

'''

# using name property without function


def disp():
    pass


t = Thread(target=disp)
t.name = 'child thread'
print('child thread name:', t.name)
# both will give same output
t.start()
print("Main thread name:", currentThread().name)
