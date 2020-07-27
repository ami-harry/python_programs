# strong tying
# we can check whether the object passed to the method has the method being invoked or not.
# hasattr() function is used to check whether the object has a method or not
# syntx --> hasattr(object,'attribute')
# where attribute can be a method or variable, if it is foung in the object then this method returns True else False

class Duck:
    def Walk(self):
        print("Duck Duck Duck")


class Horse:
    def Walk(self):
        print("hor hor hor hor")


class Cat:
    def Talk(self):
        print("mew mew mew ")


class Dog:
    def Sound(self):
        print("Bhow Bhow Bhow Bhow ")
# creating the function


def myfun(obj):
    if hasattr(obj, 'Walk'):
        obj.Walk()
    elif hasattr(obj, 'Talk'):
        obj.Talk()

    else:
        print("not found")

# passing the argument by creating the object


d = Duck()
myfun(d)

print()
h = Horse()
myfun(h)
print()
c = Cat()
myfun(c)
print()
d = Dog()  # here it will run else becuase we are not checking for sound method
myfun(d)
