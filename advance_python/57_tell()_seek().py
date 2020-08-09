# tell()--> this method is used to find current position of file pointer from beginning of the file. position starts from 0.
# syntax--> file_object.tell()

'''

f = open('harry.txt', mode='r')
print(f.tell())
data1 = f.read(5)
print(data1)
print(f.tell())
f.close()

'''

'''
# seek()--> this method is used to move the pointer from one position to another position from the beginning of the file. position starts from 0 and it must be an +ve integer

f = open('harry.txt', mode='r')
print(f.tell())  # at 0th position
data1 = f.read(5)
print(data1)
f.seek(7)  # now the pointer is on 7th position
data2 = f.read(4)  # reading 4 character after 7th position
print(data2)
print(f.tell())
f.close()

'''

