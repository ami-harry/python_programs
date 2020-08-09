# unpickling file
import pickle
import class_file

with open("data.dat", mode='rb') as harry:
    while True:
        try:
            ob1 = pickle.load(harry)
            ob1.show()
        except EOFError:
            print('Done')
            break