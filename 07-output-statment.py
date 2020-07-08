# print()
# the print() funtion is used to print the specified message to the optput screen/device.
# the message can be a string or any other object


# syntax: print(object, sep='character', end='charcater', file='sys.stdout', flush='false')
# sep= seperate the objects by given charcater. character can be any strung. default is '' or can be write none
# end= it indicate ending character for the line. default is '\n' or can write none
# file= an object with a write method. default is sys.stdout or can write none
# flush= a boolean specifying if the output is flushed(true) or buffered (false). default is false

# print()--> this function will print a empty line
# print('string')--> when a string is passed in print function the output will be the original string as it is was.

# print('hello harry')
# print()
# print("hii")
# here it will print each statement in a new line
# becuase bydefault end='\n' is working. we can manually edit it and write as end='', so the next print statement will be in the same line
# using '' or "" is same . there is no difference between both of them

# print(object) --> we can pass an object like tuple, list, dictionary to display the elements of the  object

# h=('hariom','mishti', 'shalini',50, 60.60) -->a tuple
# h1={'shalini':'keshav', 'hk':'harry', 'jk':'sk', '10':'20', '50.50':'100.50'} -->dictionary
# h2=['hariom', 'harry', 'ishrat', 10, 50.50] -->list
# print(h)
# print(h1)
# print(h2)

# print('string', sep='')--> it seperates string with given sep character. character can be any string. default '' or we can write none
# print('hi', 'hello', 'by', sep='')
# print('hi', 'hello', 'by', sep='*')
# print('hi', 'hello', 'by', sep='**')
# print('hi', 'hello', 'by', sep='***')
# generally sep is used to seperate of the spaces between the objects

# print('string', end='')--> when ending character is passed. it prints given character at the end. decault is '\n' or we can write none
# print('hello', end='\n')
# print('friends', end=' ')
# print('cahi', end=' ')
# print('p lo')

# '\t' this will gave a tab space between the objects

# print('hello', end='\t')
# print('friends', end=' \t')
# print('cahi', end='\t')
# print('p lo')
# this will print the ouput in a single line with a tab space between them


# print(variable, list) --> this is used to display the variable or also a list of variable
# print(x,y, sep=',')
# a=10
# print(a)

# a=20
# b=30
# print(a,b)
# print(a,b, sep=',')
# list of variable is printed with a single space. we can manually seperate it with using sep='' operator
# sep=',' this , will be added between the outputs
# a=10
# print('hk',a,) --> in this statement , will give a space automatically
# print('hk',a,sep='') --> here by using sep='' we are removing the space between the objects
# we can decide the nature of output by sep=''
# print('string', variable list)--> this is used to display the string along with the varible
# a=50
# print("hii i'm 50", a)
# here string is printed along the variable value a. so we can print different type of data type in a single print statement.

# age=20
# name="hariom"
# print("my name is",name, "and my age is", age)

# 