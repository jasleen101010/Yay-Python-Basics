"""
    Method overriding is an ability of any object-oriented programming language that allows a subclass or child class to
    provide a specific implementation of a method that is already provided by one of its super-classes or parent classes.
    When a method in a subclass has the same name, same parameters or signature and same return type(or sub-type) as a method
    in its super-class, then the method in the subclass is said to override the method in the super-class.
"""


# Defining Parent Class
class Parent:

    # Constructor
    def __init__(self):
        self.value = "Inside Parent"

    # Parent's show() method
    def show(self):
        print(self.value)


# Defining Child Class
class Child(Parent):

    # Constructor
    def __init__(self):
        self.value = "Inside Child"

    # Child's show() method
    def show(self):
        print(self.value)


# Driver's code
if __name__ == '__main__':
    obj1 = Parent()
    obj2 = Child()
    obj1.show()
    obj2.show()

