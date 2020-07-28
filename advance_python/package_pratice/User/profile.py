# user package-->profile module

from Tech import work  # here we are imporiting the module named work
# from Tech.work import tech_work we can do this also


def user_profile():
    print("this is from user package-->profile module")
    print("this is profile module ")
    print()


work.tech_work()  # here we are calling the method of the module
# tech_work() we can also do this


# we wish to import the work module from Tech package inside this file
# for this we have to import that file here
# fir but executing this file, we have to run this program as script and it will be run with another synatx using flag method
# it will not run in this route
# for this we have to go to parent directry and type
# python3 -m importing_package_name.module_name
# it will work


# python3 -m User.profile --> this file will run with this command
