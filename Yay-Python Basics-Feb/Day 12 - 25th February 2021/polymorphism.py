"""
The word polymorphism means having many forms.
In programming, polymorphism means same function name (but different signatures) being used for different types
"""


# Example 1
def add_nos(x, y, z = 0, az = 0):
    return x + y + z + az


print(add_nos(5, 6))
print(add_nos(5, 6, 7))
print(add_nos(5, 6, 7, 8))

# Function Overload


# Example 2
class India:
    def capital(self):
        print("India's Capital is New Delhi")


class USA:
    def capital(self):
        print("USA's Capital is Washington DC")


india = India()
india.capital()
usa = USA()
usa.capital()

# Also known as Method Overloading

# Example 3
print(len('String'))
print(len([1, 2, 3, 4, 5]))


# Example 4 [Overriding]
class Parent:

    # Constructor
    def __init__(self):
        self.value = "Inside Parent"

    # Parent's show() method
    def show(self):
        print("Parent's Method")
        print(self.value)


class Child(Parent):

    # Constructor
    def __init__(self):
        self.value = "Inside Child"

    # Child's show() method
    def show(self):
        print(self.value)


obj1, obj2 = Parent(), Child()
obj1.show()
obj2.show()

