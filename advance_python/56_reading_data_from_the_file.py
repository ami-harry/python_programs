# reading the data from the file
# read(size)--> this method is used to read data/content from a file and returns it as string in text mode or byte in binary mode

# syntax--> file_obejct.read(size)

# where size represents the number of bytes to be read from the beginning of the file
# when size is ommited or negative, the entire content of the file will be read and returned
# if the end of the file has been reached, file_object.read() will return an empty string('')

# readline() --> this method is used to read single line from a file
# syntax--> file_object.readline()


# readlines()--> this method is used to read all lines from the file
# it wil return a list of line
# syntax--> file_object.readlines()

'''
f = open('hariom.txt', mode='r')
data1 = f.read(10)  # it will read first 10 characters
data2 = f.read(10)  # it will read next 10 characters
# print(data1)
# print(data2)
for i in data1:
    print(i)
f.close()



f = open('hariom.txt', mode='r')
data = f.readline()
print(data)
f.close()


f = open('hariom.txt', mode='r')
data = f.readlines()
# print(data)
for i in data:
    print(i)
f.close()

'''