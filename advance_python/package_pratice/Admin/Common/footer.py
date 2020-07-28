# Admin package-->Common package-->footer module
import work  # after append..after refreshing it goes to up and it will create error, so before running take it down after sys.path line
import sys
sys.path.append(
    '/home/harry/Desktop/geek_py/advance_python/package_pratice/Tech/')


def admin_common_footer():
    print("this is from Admin package-->Common package -->footer package")
    print("this is footer module ")
    print()


work.tech_work()


# here we are importing the profile module of Tech package

# here we are going to use another sibling method using sys path
# we are simply going to import another file by giing its route/address
# sys.path.append(route)

# this is not  a better way to use sibling concept.
# harry@ami-harry:~/Desktop/geek_py/advance_python/package_pratice/Admin/Common$ python3 footer.py
# this will run like this
