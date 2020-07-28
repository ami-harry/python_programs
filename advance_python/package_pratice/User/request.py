# user package-->request module


from Admin.dashboard import admin_dashboard


def user_request():
    print("this is from user package-->request module")
    print("this is request module ")
    print()
    admin_dashboard()

# here we are calling the method of admin.dashboard inside the method of request module of User package
# we will call this module in another file and both the method will work

# we are importing this module in main3.py file and calling  this file
