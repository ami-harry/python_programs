# queue

from threading import Thread
from queue import Queue
from time import sleep


class Examination():
    def __init__(self):
        self.q_obj = Queue()

    def exam(self):
        for res in range(1, 11):
            print('Student ', res, ' exam fees paid')
            self.q_obj.put(res)
            print()
            sleep(2)


class Result:
    def __init__(self, ex):
        self.exam_para = ex

    def result_out(self):
        for res in range(1, 11):
            print('student ', res, ' fees recieved',
                  self.exam_para.q_obj.get(res))


e = Examination()
r = Result(e)
t1 = Thread(target=e.exam)
t2 = Thread(target=r.result_out)
t1.start()
t2.start()
