# polymorphism
# polymorphism is a word that come from two grekk word, poly means many and morpos means forms
# if a variable, object or method perform different behaviour according to situation is called polymorphism.
# Duck typing
# operator overriding
# method orveloading
# method overriding

#
# duck typing
# in python, we follow a principle ,if 'it walk like duck and talk like duck then it must be  a duck' which means python doesn't care about which class of object it is, if it is an object and required behaviour is present for the object then it will work. the type of object is distinguish only at runtime. this is called duck typing

class Duck:
    def Walk1(self):
        print("Thapak Thapak Thapak Thapak Thapak ")


class Horse:
    def Walk(self):
        print("Tabdak Tabdak Tabdak Tabdak Tabdak ")


def myfunn(arg):
    agr.Walk()


d = Duck()  # creating objects and passing it to the function as actual argument
myfunn(d)
h = Horse()
myfunn(h)
# no matter which class's object is passing in the function, it will search for the method name, if found then will run else it will show Attribute error
