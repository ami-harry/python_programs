# here we are importing the modules and its functions using syntax
# from package_name import *
# unfortunately we cant use this method in case of packages.
# before doing this we have to make a list of modules which we want to use inside __init__.py file
# __all__=[module_name]--> here we have to give those modules name which we want to impport using *


# here we have given * means those only modules will be imported which is written in the list inside __init__ module
# same name of packages will be replaced by the lastest import statement
# for acessing those we must give a nickname for those modules
from Admin import *
# because logout named module is in Tech and User package too
from Admin import logout as lg
from Admin.Common import *
from Tech import *
# becuase same name of module is in User package so we are giving them a nick name
from Tech import logout as lgt, profile as pft

from User import *

# accessing the modules of Admin Package
dashboard.admin_dashboard()  # accessing using the module.fun_name()
lg.admin_logout()
product.admin_product()
service.admin_service()

# accessing the modules of Common package of Admin Package
footer.admin_common_footer()
header.admin_common_header()

# accessing the modules of Tech Package
lgt.tech_logout()
pft.tech_profile()
# these are replaced by user becuase the moodule name is same, we need to give a  nick name for the same name of packages
work.tech_work()

# accessing the modules of User Package
logout.user_logout()
profile.user_profile()
request.user_request()
