
# main file
# here we will import both modules, first and second
# --> in both modules, the variable names and function name are same.
'''

import first
import second

print(first.a)
print(second.a)

first.name()
second.name()

'''


'''

# accessing it with aliasing

import first as f
import second as s

print(f.a)
print(s.a)

f.name()
s.name()

'''
'''


# accessing it using from module_name import var, fun type
from first import a, name
print(a)
name()

# here it will print first module data

from second import a, name

# here it will print second module value

# becuase the name is same same so second will replace the first module if(from first import a, name
#  from second import a, name)
print(a)
name()

'''

'''

# accessing it using from module_name import var, fun type as alias_name

from first import a, name , tup as tp
from second import a, name as np , lst as lt

print(a) # it will print second method becuse it will replce first becuase of same nane
print(lt)
print(tp)
name()
np()
'''



