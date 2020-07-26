# constructor overriding

# if we write consider in both the classes, parent class and child class then the parent class constructor is available to the child
# in this case olny chid class constructor is accessible which means child class constructor is replacing parent  class constructor.

# constructor overriding is used when programmer want to modify the existing behaviour of constructor


class Father:
    fp = 'yes'

    def __init__(self):
        self.price = 65432
        print("parent constructor is called")

    def show_price(self):
        print("Price in father class:", self.price)

    @classmethod
    def class_val(cls):
        print("class value:", cls.fp)


class Son(Father):
    def __init__(self):
        self.model = 'nokia 6.1+'
        print("child constructor is called")

    def show_model(self):
        print("model in child class:", self.model)
        # print("prince in parent class:", self.price) #

    @classmethod
    def class_child(cls):
        print("class value in child class through parent class:", cls.fp)


# here the parent construcor will be escaped by the child constructor.
c = Son()  # here the constructor will be called
c.show_model()
# c.show_price()
c.class_child()
c.class_val()
print(c.fp)

f=Father()