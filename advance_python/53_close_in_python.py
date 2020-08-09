# close()
#
# # # Python file method close() closes the opened file. A closed file cannot be read or written any more. Any operation, which requires that the file be opened will raise a ValueError after the file has been closed. Calling close() more than once is allowed.
#
# # Python automatically closes a file when the reference object of a file is reassigned to another file. It is a good practice to use the close() method to close a file.
#
# Syntax
# Following is the syntax for close() method −
#
# fileObject.close()

# closed--> this is used to check whether fle is closed or not. it shows True if the file is close else False
# syntax--> file_object.closed

# file_onject_method

# readable()--> this method is used to check whether file is readable or not. it returns True if the file is readable else False
# syntax--> file_onjecct.readable()


# writble()--> this method is used to check whether file is writable or not. it returns True if the file is readable else False
# syntax--> file_onjecct.writable()


print("read mode")
f = open('harry.txt', mode='r', encoding='utf-8')
print('filename:', f.name)
print('readable:', f.readable())
print('writable:', f.writable())
print('file closed:', f.closed)
f.close()
print('file closed:', f.closed)


print()

print("write mode")
f = open('hk.txt', mode='w', encoding='utf-8')
print('filename:', f.name)
print('readable:', f.readable())
print('writable:', f.writable())
print('file closed:', f.closed)
f.close()
print('file closed:', f.closed)
print()

print("append mode")
f = open('hk.txt', mode='a', encoding='utf-8')
print('filename:', f.name)
print('readable:', f.readable())
print('writable:', f.writable())
print('file closed:', f.closed)
f.close()
print('file closed:', f.closed)
