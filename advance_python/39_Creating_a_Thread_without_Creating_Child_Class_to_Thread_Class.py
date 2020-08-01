# Creating_a_Thread_without_Creating_Child_Class_to_Thread_Class
# we can create an independent thread child class that does not inherit from thread class
'''
from threading import *


class MyClass:
    statement


object_name = MyClass()
Thread_object=Thread(target=object_name.functionName,args=(arg1,arg2..))
Thread_object.start()
'''
'''


from threading import Thread


class MyClass:
    def disp(self, a, b):
        print(a, b)


obj = MyClass()
t = Thread(target=obj.disp, args=('hello', 'harry'))
t.start()

'''