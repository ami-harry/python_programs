# pickling file

import pickle
import main_class


n = int(input("Enter number of students: "))
with open('harry.dat', mode='wb') as hk:
    for data in range(n):
        name = input("Enter your name: ")
        age = int(input("Enter your age: "))
        roll = int(input("Enter your roll: "))
        address = input("Enter your address: ")
        ob = main_class.Student(name, age, roll, address)
        pickle.dump(ob, hk)
    print("Data pickled sucessfully\n")
