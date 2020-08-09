import class_data
import pickle

with open('laptop.dat', mode='rb') as laptop:
    while True:
        try:
            data = pickle.load(laptop)
            data.show_details()
            print()
        except EOFError:
            print("Done")
            break
