#  Single_Tasking_using_a_Thread
# When multiple task are executed by thread one by one, then it is called single tasking

# ex--> writing examination
# question 1
# question 3
# question 3
# ....


from threading import Thread
from time import sleep

'''
class Myclass:
    def solve_question(self):
        self.q1()
        self.q2()
        self.q3()
        self.q4()
        self.q5()

    def q1(self):
        print("question 1 solved")
        sleep(2)

    def q2(self):
        print("question 2 solved")
        sleep(2)

    def q3(self):
        print("question 3 solved")
        sleep(2)

    def q4(self):
        print("question 4 solved")
        sleep(2)

    def q5(self):
        print("question 5 solved")


obj = Myclass()
t = Thread(target=obj.solve_question)
t.start()
t.join()
print("all questions are solved")

'''


class MyProblem:
    def problem(self):
        self.p1()
        self.p2()
        self.p3()
        self.p4()
        self.p5()
        self.p6()
        self.p7()
        self.p8()
        self.p9()
        self.p10()

    def p1(self):
        print("problem 1 solved")
        sleep(2)

    def p2(self):
        print("problem 2 solved")
        sleep(2)

    def p3(self):
        print("problem 3 solved")
        sleep(2)

    def p4(self):
        print("problem 4 solved")
        sleep(2)

    def p5(self):
        print("problem 5 solved")
        sleep(2)

    def p6(self):
        print("problem 6 solved")
        sleep(2)

    def p7(self):
        print("problem 7 solved")
        sleep(2)

    def p8(self):
        print("problem 8 solved")
        sleep(2)

    def p9(self):
        print("problem 9 solved")
        sleep(2)

    def p10(self):
        print("problem 10 solved")


mp = MyProblem()
t = Thread(target=mp.problem)
t.start()

# solving the problem with some time delay
