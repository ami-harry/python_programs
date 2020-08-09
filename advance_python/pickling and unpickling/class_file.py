# class file

class Student:
    def __init__(self, st_name, st_roll, st_address):
        self.name = st_name
        self.roll = st_roll
        self.college = st_college

    def show(self):
        print(f"Name:{self.name} Roll:{self.roll} Address:{self.college}")


# this class will be used to pickling and unpickling purpose by importing this into those files
