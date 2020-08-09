# pickling and unpicking

# picking
# pickling is a process of conveting a calss object into a byte stream so that it can be stored into a file. this is also called as object serialisation.
# we use pickle module to prefrom pickling and unpickling

# function
# dump()--> this function is used to perfrom the pickling , it returns the pickled represensation og the object as a byte object instead of writing it to a file. this method belongs to pickle module
# syntax--> import pickle
# pickle.dump(obj,filename)


# unpickling
# unpickling is a process whereby byte stream is converted back into a class object. it is inverse operaion of pickling. this is also called as de-serilisation. pickling and unpickling should be done using binary files since they support byte streams
# we use pickle module to perform pickling and unpickling

# warining--> the pickle module is not secure aggainst errorneous or maliciously constructed data. never unpickle data recieved from an untrusted or aunauthorised source


# function
# load()--> this function is used to read an pickled object from a binary file and returns it into object, this method belongs to pickle module.
# import pickle
# pickle.load(file)


# why do we need pickling and unpickling
# when we store some structured data in the fie and want to perform calcultion that time we need pickling and unpickling


import pickle


class Student:
    def __init__(self, st_name, st_roll, st_address):
        self.name = st_name
        self.roll = st_roll
        self.address = st_address

    def show(self):
        print(f"Name:{self.name} Roll:{self.roll} Address:{self.address}")


# writing data into a binary file
with open('pickling.dat', mode='wb') as hk_load:
    # creating the object of the class
    st = Student('hariom', 54, 'Patna')
    pickle.dump(st, hk_load)
    print('data pickkled sucessfully')

# printing the data using calling the class method

with open('pickling.dat', mode='rb') as hk_read:
    data = pickle.load(hk_read)
    print('data unpickled sucessfully')
    # calling the class method using returned pickle method
    data.show()
    # print('data pickkled sucessfully')

# printing the data using calling the class method

with open('pickling.dat', mode='rb') as hk_read:
    data = pickle.load(hk_read)
    print('data unpickled sucessfully')
    # calling the class method using returned pickle method
    data.show()
