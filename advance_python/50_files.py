# files
# file is a collection of data that is available to a program. we can retreive and use data stored in a file whenever we required.

# advantages
# stored data is permanently unless someone remove it
# stored data can be shared
# it is possible to update or remove the data


# types of data
# there are two type of file
# text-file--> it stores data in the form of characters. it used to stores characters and strings
# binary file--> it stores data in the form of bytes, a group of 8 bits each. it is used to store txt,img,pdf,csv ,mp4 files...


# text mode and binary mode
# text mode
# a file opened in text mode, treats its content as if it contaiins text strings of the str type
# when you get data from a text mode file, first python file decodes the row bytes using either a plateform dependent encoding ot specific one

# binary code--> a file opened in binary mode, python uses the data in the file without using any decoding, binary mode file reflects the raw data in the file.


# opening  a file in wrtite mode, if the files doesn't exits, then it will create it and write in it
f = open('harry.txt', mode='w')
f.write("Hello \n")
f.write("Harry \n")
f.write("How are you ")
f.close()
# here we have created a text file


# reading the file in text mode
f = open('harry.txt', mode='r')
data = f.read()  # reading and storing the data in a  variable
print(data)  # printing the data
f.close()  # closing the file


print()

# reading the file in binary mode
f = open('harry.txt', mode='rb')
data = f.read()  # reading and storing the data in a  variable
print(data)  # printing the data
f.close()  # closing the file
