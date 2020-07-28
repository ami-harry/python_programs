# main_importing_class --> here we are importing methods having class

"""
import fclass

# to import class the syntax is
# object=module_name.class_name()

m = fclass.Myclass()
m.name()
m.show()
print()
s = fclass.School()
s.name()
s.show()

# here we are making the class in another file and making its object and accessing it by importing that file here
# we can also use the concept of inheritnce through this


"""
"""


# importing two classes

import fclass
import sclass

m = fclass.Myclass()
m.name()
m.show()
print()
s = fclass.School()
s.name()
s.show()
#
print()
sc = sclass.Mycollege()
sc.show()

"""
"""


# when the both modules have the same class name then?

import fclass
import sclass

mc=fclass.Myclass()
mc.name()
mc.show()
print()
ms=fclass.School()
ms.name()
ms.show()

# importing from second file, having the class name is same

print()
mc=sclass.Myclass()
mc.name()
mc.show()
print()
ms=sclass.School()
ms.name()
ms.show()
print()
mss=sclass.Mycollege()
mss.show()
"""
"""


# importing from module with class name


# object of second file,, becuse of same name,, second will replace first, this can be solved by giving them as alisaing name
from fclass import Myclass, School
from sclass import Myclass, School, Mycollege
mc = Myclass()
mc.show()

mclg=Mycollege()
mclg.show()
print()
"""

# importing from module with class name with aliasing

# from fclass import Myclass, School
from sclass import Myclass as sc, School as ss, Mycollege

# here the same name class is given to a nickname , so we can easily access them

# fcls=Myclass()
# fcls.show()
# print()
# fcls.name()
# s=School()
# s.show()
# print()
# s.name()
# print()

s=Mycollege() #myclass of second file
s.show()
print()
s1=sc()
s1.name()
s1.show()


print()
s2=ss()
s2.show()
s2.name()