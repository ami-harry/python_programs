# unpickling file

import pickle
import main_class

with open('harry.dat', mode='rb') as hk:
    while True:
        try:
            data = pickle.load(hk)
            data.show()
            print()
        except EOFError:
            print("Done")
            break
    print("Data unpickled sucessfully")
