# here we are imporiting the request module of User packge
# by calling the method of that module another method of another module will also called
# inside the function of request module of User packge a function is calling of dashboard module of Admin package
# both will be called


# from User.request import user_request  # here we have imported the method
# user_request()  # executing the method

from User import request as r
import User as ug
import User
from User import *
from User import request
request.admin_dashboard()

request.admin_dashboard()

User.request.user_request()

ug.request.user_request()

r.admin_dashboard()

request.admin_dashboard()


# all of them will work
