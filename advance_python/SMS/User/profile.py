# user package--> profile module
# importing the function of profile module of Tech package

from Tech.profile import tech_profile
# here we are imporitng the function of module profile of tech package


def user_profile():
    print("user package--> profile module")
    print("user_profile() function")
    print()
    tech_profile()  # importing this file in main file, by calling this function the user function will also be called,, we accessing the module of Tech package inside module of User package and using User package we importing its module in main file and accessing tech and user package and its modules

# accessing the function
# python3 -m Tech.profile


# tech_profile()
