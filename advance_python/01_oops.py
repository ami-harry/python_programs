# advance python

# Object oriented programming
# object oriented programming (OOP) is a programming language model organized around objects rather than 'actions' and data rahter than 'logic'

# concept of oops
# a. Encapsulation
# b. Abstraction
# c. Inheritance
# d. Polymorphism

# Encapsulation
# Encapsulation means that the internal representation of an object is generlly hidden from view outside of the object definition. a class is an example of encapsulation as it Encapsulates all the data that is member function, variable etc..


# Abstraction
# Abstraction in Python is the process of hiding the real implementation of an application from the user and emphasizing only on uses of it
# basically abstraction focuses on hiding the internal implementation of a process or method from the user. in this way the user knows what he is doing but not know how actually it is happenning or getting  completed.

# Inheritance
# Inheritance allows us to define a class that inherits all the method and properties from another class. parent class is the class being inherited from, also called base class, child class is the inherits from another class also called derived class


# Polymorphism
# Polymorphism in pyhton, defines method in the child class that have the same name as the method in the parent class, in inheritance the child class inherits the methods from the parent class, also is is possible to modify a method in a child class that it has inherited from the parent class.


# Class
#  a python class is a group of attrubutes and methods

# what is attribute?
# attributes are represented by variable that contains data

# what is method?
# method performs an action or task, it is similar to function


# how to create a class
# class class_name(object):
# def __init__(self, formal_arguments):
# self.variable_name = value
# self.variable_name1 = 'value'
#
# def method_name(self, formal_arguments):
# local_variables
# body of method..

# here __init__(self) is constructor method
# we can write object inside the class or can avoid it, becuase it is bydefault


# class--> class keyword is used to create a class

# object--> object represnts the base class name from where all classes in python are derived. this class is also derived from object class. this is optionl

#  __init__--> This method is used to initialize the variable . this is a special method, we do not call the method explicitly

# self--> self is a variable which refers to current class object/instance.


# Rules
# the class name can be any valid integer
# it caan not be any python reserved word
# a valid class name starts with a letter followed by any no of letters, nunbers, or underscores
# a class name generally starts with capital letter.


# Object
# object is class type variable or class instance. to use a class , we should create an object to the class
# instance/object creation represents alloting memory necessary to store the actual data of the variable.
# each time you create an object of a class of each variable defined in the class is created.
# in other words you can say that each object is created has its own copy of data members defined in the class.

# object_name=class_name()
# object_name=class_name(arguments)


# without argument
# class mobile():
# def __init__(self):
# self.model = 'nokia 6.1+'
#
# def show_model(self):
# print("model:", self.model)
#
#
# creating an object for class mobile
# nokia = mobile()  # this is without argument

################################################


# with argument
# class mobile():
#     def __init__(self, arg1):  # here it is formal argument
#         self.model = arg1

#     def show_model(self):
#         print("model:", self.model)


# creating an object for class mobile
# nokia = mobile('nokia 6.1_')  # actual argument


# how it works
# nokia = mobile()
# a block of memory is allocated on heap. the size of allocated is to be decided from the attributes and moethods available in the class(mobile)
# after allocating memory block, the special method __init__() is called internally. this method stores the intial data into variables.
# the allocated memory location address of the instance is returned into object (nokia)
# the memory location is passes to self

# accessing class member using object
# we can access variable and method of a class using class object or instance of class
# object_name.variable_name
# object_name.method_name()
# object_name.method_name(100)#with parameter

# self-variable
# self is a default variable that contains the memory address of the current object
# this variable is used to refer all the instance variable and method
# when we create object of a class the object name contains memory location of the object
# this memory location is internally passed to self as self knows the memory address of the object so we can access variable and method of object
# self is the first argument to any object method becuase the first argument is always the object refrence. this is automatic, whether you call it or not it calls itself
# def __init__(self):
# def method(self):

# each time when we create an object if a class, a copy of each variable deined in the class is created.
# on modifying in any variable will not affect on other, becuase  both have own memory location.

