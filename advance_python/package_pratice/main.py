# importing the packages and its module
# syntax is from package_name import module

# if two modules have same name then the recent called will replace the previous call, so for more convient give it as aliasing name to access it properly
from Admin import service, dashboard, logout, product
from Admin.Common import header, footer
from Tech import logout as lg, profile as pf, work
from User import logout as lgu, profile as pfu, request
# accessing the modules and methods of Admin package
service.admin_service()
dashboard.admin_dashboard()
logout.admin_logout()
product.admin_product()

# accessing the modules and methods of Common package of Amdmin package
header.admin_common_header()
footer.admin_common_footer()

# accessing the modules and methods of Tech package
lg.tech_logout()
pf.tech_profile()
work.tech_work()

# accessing the modules and methods of User package
lgu.user_logout()
pfu.user_profile()
request.user_request()
