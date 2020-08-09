# check file exits or not
# isfile()--> this method is used to check whether specified file is exists or not. this method belongs to path module which is sub modules of os module.
# syntax -->
# import os
# os.path.isfile(filename)


import os

if os.path.isfile('harry.txt'):
    f = open('harry.txt')
    print("File opened sucessfully")  # giving sucess message
    f.close()

else:
    print("File not found")
