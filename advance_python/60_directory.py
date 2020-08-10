# directory
# os module--> this module is used to perform simple operation on directories. this module represents operating system dependent functionality.

# getcwd()--> this method is used to know the current woriking directory
# os.getcwd()

# makedir('ParentDir/ChildDir/GrandChildDir')--> this method is used to recursively create sub-directories

# removedirs('DirName')--> this method is used to recursively remove all dirctories.
# syntax--> os.removedirs('ParentDir/ChildDir/GrandChildDir')

# walk()--> this method is used to know contents of a directory including sub-directory. is returns an iterator object whose content can be displayed using for loop. the iterator object contains directory path/ dir name/ file name found in the specific directories

# syntax--> os.walk(path, topdown=True,Onerror=None,followlinks=False)
# path--> it represents the dir name, we can write dot(.) to specify current directory
# topdown()--> if it is True the dir and its sub dir are traversed in topdown manner. if it is false then the directory and its sub directory are traversed in bottom-up manner.
# Onerror--> True to visit directories pointed to by symbolic's liks on system that support them. if False walk() wait not walk down into symbolic links that resolve to directories


import os
# print(os.getcwd())  #---> printing current working directory

# os.mkdir('harry')  #---> this will create a new directory

# --->this will create a new directory inside the parent directory
# os.mkdir('harry/hk1')

# to make directories inside directory without having parent directory
# os.makedirs('ha/ri/om/k/u/m/a/r')  # this will create dir inside dir

# changing the directory
# print(os.getcwd())  # ---> printing current working directory
# os.chdir('harry')  # the current working dir will be changed to harry
# print(os.getcwd())  # ---> printing current working directory


# renming the dir
# os.rename('ha', 'hariom')  # this will change the folder ha with hariom name
# old = ['hariom', 'harry', 'SMS']
# new = ['1', '2', '3']
# this will change the folder ha with hariom name
# os.renames(old=('hariom', 'harry', 'SMS'), new=('1', '2', '3'))


# removing the dir
# os.rmdir('harry/hk1')  # --> this  will remove the dir hariom
# os.rmdir('harry')  # --> this  will remove the dir hariom
# os.mkdir('hariom')
# os.makedirs('hariom/ri/om/k/u/m/a/r')
# os.removedirs('hariom/ri/om/k/u/m/a/r')


# walk()  --> ('.') dot means current directory
'''
walk_bj = os.walk('.')
for data in walk_bj:
    print(data, end='\n\n')

'''
# extracting all the contents of SMS directory
data = os.walk('SMS', topdown=False)
for dir in data:
    print(dir, end='\n\n')


