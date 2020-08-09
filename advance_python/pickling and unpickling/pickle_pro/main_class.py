# main_class file

class Student:
    def __init__(self, name, roll, age, address):
        self.st_name = name
        self.st_roll = roll
        self.st_age = age
        self.st_address = address

    def show(self):
        print(
            f"Name: {self.st_name}  Roll: {self.st_roll}  Age: {self.st_age}  Address: {self.st_address}")
