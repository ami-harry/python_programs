# pickling file
import pickle
import class_file

n = int(input("Enter how many students you want to add: "))
with open("data.dat", mode='wb') as harry:
    for data in range(n):
        name = input("Enter student name: ")
        roll = int(input("Enter student roll: "))
        college = input("Enter college name: ")
        obj = class_file.Student(name, roll, college)
        pickle.dump(obj, harry)
    print("File Dump sucessfully")
# here we have pickled our data , in the next file we will unpickle this data
