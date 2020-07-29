# here the example of interface
# with army and gun example
# here the gun ,area, salary ,dress will be different for all of them
# these 4 functions will be different for each of them and will be deined in their respctive classes


from abc import ABC, abstractmethod


class DefenceForce(ABC):
    @abstractmethod
    def salary(self):
        pass

    @abstractmethod
    def dress(self):
        pass

    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def gun(self):
        pass

# these are thhe abstract method and DefenceForce is an interface, defining its methods in their respective child classes


class Army(DefenceForce):
    def salary(self):
        # here we can make its own abstract method and static method for other purpose
        print('this is army class')
        print('defining salar of DefenceForce class')
        print('salary:45678')

    def dress(self):
        print('this is army class')
        print('defining salar of DefenceForce class')
        print('dress:dark-khaki')

    def area(self):
        print('this is army class')
        print('defining salar of DefenceForce class')
        print('area:Land')

    def gun(self):
        print('this is army class')
        print('defining salar of DefenceForce class')
        print('gun:AK47')

# we can access all the method by making its object


class AirForce(DefenceForce):
    def salary(self):
        # here we can make its own abstract method and static method for other purpose
        print('this is AirForce class')
        print('defining salar of DefenceForce class')
        print('salary:56433')

    def dress(self):
        print('this is AirForce class')
        print('defining salar of DefenceForce class')
        print('dress:light-sky')

    def area(self):
        print('this is AirForce class')
        print('defining salar of DefenceForce class')
        print('area:Sky')

    def gun(self):
        print('this is AirForce class')
        print('defining salar of DefenceForce class')
        print('gun:AK31')

# we can access all the method by making its object


class Navy(DefenceForce):
    def salary(self):
        # here we can make its own abstract method and static method for other purpose
        print('this is Navy class')
        print('defining salar of DefenceForce class')
        print('salary:65434')

    def dress(self):
        print('this is Navy class')
        print('defining salar of DefenceForce class')
        print('dress:light-blue')

    def area(self):
        print('this is Navy class')
        print('defining salar of DefenceForce class')
        print('area:Sea')

    def gun(self):
        print('this is Navy class')
        print('defining salar of DefenceForce class')
        print('gun:AK57')

# we can access all the method by making its object


a = Army()  # making object and accessing all the method, if there is any constructor then it will execute here
af = AirForce()  # making object and accessing all the method, if there is any constructor then it will execute here
n = Navy()  # making object and accessing all the method, if there is any constructor then it will execute here

print()
a.area()
print()
a.dress()
print()
a.gun()
print()
a.salary()
print()
af.area()
print()
af.dress()
print()
af.gun()
print()
af.salary()
print()
n.area()
print()
n.dress()
print()
n.gun()
print()
n.salary()
print()


# trying to access this file in 26_interface.py
#  using import module concept
