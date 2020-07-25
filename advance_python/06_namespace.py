# namespace
# in python , namespace represents a memory block where names are mapped to objects

# class namespace:
#  a class maintains it's own namespace known as class namespace. in this class namespace the names are mapped to class variable

# instance namespace
# every instance have its own namespace known as instance namespace. in this instance namespace, the names are mapped to instance variable

'''
class Mobile:
    fp = 'yes'


nokia = Mobile()
lenovo = Mobile()
moto = Mobile()

# here 'yes' is class name space and fb class variable is also mapped with the class namespace
# nokia, lenovo, moto,,,, are instance namespace are mapped with same value 'yes'


Mobile.fp  # accessing class variable with class name
nokia.fp  # accessing class variable using object
lenovo.fp
moto.fp

# all will give same output becuase all are tagged with the class variable

# if we modify the class variable, then all the values will be affected
Mobile.fp = 'harry'  # this will affect on all objects

# if we modify any object then only that object will get affected and remaining will have the same value as class name
# this will be affected only on nokia object and remaining have the same value as they have before this modification
nokia.fp = 'this is changed'
'''


# class variable-namespace
class Mobile:
    fp = 'yes'

    @classmethod
    def is_fp(cls):
        print("fingerprint:", cls.fp)


nokia = Mobile()
lenovo = Mobile()
moto = Mobile()

# printing the values
print("before modification")
print("class fp", Mobile.fp)
print("Nokia", nokia.fp)
print("lenovo", lenovo.fp)
print("moto", moto.fp)
print()
print("after modification in class variable")
Mobile.fp = 'no'
# this will be affected on all others objects

print("class fp", Mobile.fp)
print("Nokia", nokia.fp)
print("lenovo", lenovo.fp)
print("moto", moto.fp)

print()
print("after modification in single object")
nokia.fp = 'not working'
# it will be only affected on this object,..remaining will have their previous value
print("class fp", Mobile.fp)
print("Nokia", nokia.fp)
print("lenovo", lenovo.fp)
print("moto", moto.fp)
