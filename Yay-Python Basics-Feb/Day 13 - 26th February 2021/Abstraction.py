# Abstraction

""" Definition
Abstraction means hiding the complexity and only showing the essential features of the object.
So in a way, Abstraction means hiding the real implementation and we, as a user, knowing only how to use it.

Real world example would be a vehicle which we drive without caring or knowing what all is going underneath.

A TV set where we enjoy programs with out knowing the inner details of how TV works.
"""

"""
Abstraction in Python is achieved by using abstract classes and interfaces.

An abstract class is a class that generally provides incomplete functionality and contains one or more abstract methods. 
Abstract methods are the methods that generally don’t have any implementation, 
it is left to the sub classes to provide implementation for the abstract methods.


An interface should just provide the method names without method bodies. Subclasses should provide implementation for 
all the methods defined in an interface. Note that in Python there is no support for creating interfaces explicitly, 
you will have to use abstract class. In Python you can create an interface using abstract class. 
If you create an abstract class which contains only abstract methods that acts as an interface in Python.
"""

"""
By default, Python does not provide abstract classes. Python comes with a module which provides the base for defining 
Abstract Base classes(ABC) and that module name is ABC. ABC works by decorating methods of the base class as abstract 
and then registering concrete classes as implementations of the abstract base. A method becomes abstract when decorated 
with the keyword @abstractmethod. 
"""

# Importing Library for Abstraction
from abc import ABC, abstractmethod

# Example 1


# # Abstract Class `Polygon`
# class Polygon(ABC):
#
#     # Abstract Method
#     @abstractmethod
#     def noOfSides(self):
#         pass
#
#
# # Inherited Class `Triangle`
# class Triangle(Polygon):
#
#     # Overriding Abstract Method
#     def noOfSides(self):
#         print("I've 3 Sides!")
#
#
# # Inherited Class `Pentagon`
# class Pentagon(Polygon):
#
#     # Overriding Abstract Method
#     def noOfSides(self):
#         print("I've 5 Sides!")
#
#
# # Inherited Class `Hexagon`
# class Hexagon(Polygon):
#
#     # Overriding Abstract Method
#     def noOfSides(self):
#         print("I've 6 Sides!")
#
#
# # Driver Code [Main Method]
# if __name__ == '__main__':
#
#     R = Triangle()
#     R.noOfSides()
#     P = Pentagon()
#     P.noOfSides()
#     H = Hexagon()
#     H.noOfSides()


# Example 2


# # Abstract Class `Animal`
# class Animal(ABC):
#
#     # Abstract Method
#     @abstractmethod
#     def move(self):
#         pass
#
#
# # Inherited Class `Human`
# class Human(Animal):
#
#     # Overriding Abstract Method
#     def move(self):
#         print("I can Walk and Run")
#
#
# # Inherited Class `Snake`
# class Snake(Animal):
#
#     # Overriding Abstract Method
#     def move(self):
#         print("I can Crawl")
#
#
# # Inherited Class `Dog`
# class Dog(Animal):
#
#     # Overriding Abstract Method
#     def move(self):
#         print("I can Bark")
#
#
# # Inherited Class `Lion`
# class Lion(Animal):
#
#     # Overriding Abstract Method
#     def move(self):
#         print("I can Roar")
#
#
# # Driver Code [Main Method]
# if __name__ == '__main__':
#
#     obj = Human()
#     obj.move()
#     objD = Dog()
#     objD.move()
#     objS = Snake()
#     objS.move()
#     objL = Lion()
#     objL.move()


# Example 3


# Abstract Class `Payment`
class Payment(ABC):

    # Static Method `Print Slip`
    @staticmethod
    def print_slip(amount):
        print(f"Purchase of Amount: ${amount}")

    # Abstract Method `Payment`
    @abstractmethod
    def payment(self, amount):
        pass


# Inherited Class `CreditCardPayment`
class CreditCardPayment(Payment):

    # Overriding Abstract Method
    def payment(self, amount):
        print(f"Credit Card Payment of : ${amount}")


# Inherited Class `MobileWalletPayment`
class MobileWalletPayment(Payment):

    # Overriding Abstract Method
    def payment(self, amount):
        print(f"Mobile Wallet Payment of : ${amount}")


# Driver Code [Main Method]
if __name__ == '__main__':

    obj = CreditCardPayment()
    obj.payment(100)
    obj.print_slip(100)
    print(isinstance(obj, Payment))
    print(isinstance(obj, CreditCardPayment))
    print(isinstance(obj, MobileWalletPayment))
    obj1 = MobileWalletPayment()
    obj1.payment(200)
    obj1.print_slip(200)
    print(isinstance(obj1, Payment))
    print(isinstance(obj1, CreditCardPayment))
    print(isinstance(obj1, ABC))
