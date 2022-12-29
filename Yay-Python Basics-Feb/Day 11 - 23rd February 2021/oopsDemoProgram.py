# A Random Class
class Random_Class:

    # Class Variables
    a = 1
    b = 2
    c = 3

    # Constructor
    def __init__(self, x0):                # Such Methods are known as DUNDER Methods.

        # Instance Variables
        self.x = x0
        self.y = 2

    # Instance Methods
    def instanceMethods(self):
        print(f"Value of X: {self.x}")

    # Class Methods
    @classmethod                           # -> Decorator
    def classMethods(cls):
        print(f"Value of a: {cls.a}")


# This is also a Class
class classExample:
    pass


# Running Main Method
if __name__ == '__main__':

    # Instantiating `classExample`
    obj = classExample()
    # print(locals())

    # Instantiating a Class
    obj1 = Random_Class(99)
    # obj1.instanceMethods()
    # obj1.classMethods()

    obj2 = Random_Class(10)
    obj2.instanceMethods()
    obj2.classMethods()

    print("Old Object")
    obj1.instanceMethods()
    obj1.classMethods()


