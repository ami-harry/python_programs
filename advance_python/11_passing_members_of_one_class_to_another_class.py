# passing membres of one class to another class

# members(attributes and methods)

class Student:
    # constructor
    def __init__(self, n, r):
        self.name = n
        self.roll = r

    # instance method
    def show(self):
        print("Student name: ", self.name)
        print("Student roll: ", self.roll)


class User:
    @staticmethod
    def sh(s):
        print('user name: ', s.name)
        print('user roll: ', s.roll)
        s.show()  # calling the method of another class inside static method class


# making an object of class student and passing the arguments
stu = Student('harry', 21)
# calling the static method and passing the object of another class as its parameter
User.sh(stu)  # calling the static method and passing its parameter
