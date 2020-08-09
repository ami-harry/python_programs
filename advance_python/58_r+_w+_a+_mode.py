# r+ / a+ / w+ mode

'''
# r+ mode
# read then write


f = open('harry.txt', mode='r+')
print(f.tell())  # initially it is at 0th position
data = f.read()  # reading the data
print(f.tell())  # it will on the last char no
f.write('\n hello harry, this line is adding')  # adding the data
print(f.tell())  # it will be on the last char after writing
print(data)  # it will print the old data before writing, becuase we have read the data before writing
print(f.tell())  # it is no at the end of the file
# to print all the data, we have to move our cursor to the staring point so we can read all the data
f.seek(0)
data1 = f.read()
print(f.tell())
print(data1)
print(f.tell())
f.close()

'''

'''

# a+ mode
# appending then reaing the file, it will not override the previous data
f = open('harry.txt', mode='a+')
print(f.tell())
f.write('\nThis is appending through a+ mode\n')
print(f.tell())
data = f.read()
print(f.tell())
print(data)
print(f.tell())
f.seek(0)  # taking the pointer to the beginning
print(f.tell())
data1 = f.read()
print(f.tell())
print(data1)
print(f.tell())
f.close()

'''

'''
# w+ mode
# writing then reaing the file, it will override the previous data
f = open('hariom.txt', mode='w+')
print(f.tell())
f.write('\nThis is appending through w+ mode\n')
print(f.tell())
data = f.read()
print(f.tell())
print(data)
print(f.tell())
f.seek(0)  # taking the pointer to the beginning
print(f.tell())
data1 = f.read()
print(f.tell())
print(data1)
print(f.tell())
f.close()

'''

