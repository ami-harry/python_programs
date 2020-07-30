# sleep method
# sleep() method is used to stop the execution of program temprorily for a given amount of time. when this function is called, PVM stops program for given amout of time
# it belongs to time module

import time
for i in range(20):
    print(i)
    if(i == 10):
        time.sleep(2.5)  # it will stop for 2.5 seconds when i=10
