# here we are importing the modules and its functions using syntax
# from package_name.module_name import method_name

from Admin.dashboard import admin_dashboard
from Admin.logout import admin_logout
from Admin.product import admin_product
from Admin.service import admin_service
from Admin.Common.footer import admin_common_footer
from Admin.Common.header import admin_common_header
from Tech.logout import tech_logout
from Tech.profile import tech_profile
from Tech.work import tech_work
from User.logout import user_logout
from User.profile import user_profile
from User.request import user_request

# accessing the method of module of Admin package
admin_dashboard()
admin_logout()
admin_product()
admin_service()

# accessing the method of module of Admin.Common package
admin_common_footer()
admin_common_header()

# accessing the method of module of Tech package
tech_logout()
tech_profile()
tech_work()

# accessing the method of module of User package
user_logout()
user_profile()
user_request()
