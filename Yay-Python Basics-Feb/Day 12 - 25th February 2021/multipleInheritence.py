# Defining Parent Class 1
class Parent1:

    # Parent's Show Method
    def show(self):
        print("Inside Parent 1")

    # Same Method for Every Class
    def constant(self):
        print("Parent1 Method")


# Defining Parent Class 2
class Parent2:

    # Parent's Show Method
    def show(self):
        print("Inside Parent 2")

    # Same Method for Every Class
    def constant(self):
        print("Parent2 Method")


# Defining Child Class
class Child(Parent1, Parent2):                   # Who-so-ever will be occurring first in the argument will be given priority in case of super()

    # Child's Show Method
    def show(self):
        print("Inside Child")

    # Same Method for Every Class
    def constant(self):
        super().constant()
        Parent2().constant()
        print("Child Method")


# Driver Code
if __name__ == '__main__':
    obj = Child()
    obj.show()
    obj.constant()


