"""
    Dunder or magic methods in Python are the methods having two prefix and suffix underscores in the method name.
    Dunder here means “Double Under (Underscores)”. These are commonly used for operator overloading.
    Few examples for magic methods are: __init__, __add__, __len__, __repr__ etc.

    Dunder methods can be used to emulate behaviour of built-in types to user defined objects and is core Python feature
    that should be used as needed.
"""


# Class String
class String:

    """
    A Basic User-Defined DataType by using Class
    """

    """
    The above snippet of code prints only the memory address of the string object class.
    """

    # Constructor
    def __init__(self, string, my_list = []):
        self.string = string
        self.my_list = my_list

    """
    The above snippet of code prints only the memory address of the string object class.
    """

    def __str__(self):
        print("STR!!!")
        return 'Object: {}'.format(self.string)

    def __repr__(self):
        print("REPR!!!")
        return 'Object: {}'.format(self.string)

    def __add__(self, other):
        return self.string + other

    def __len__(self):
        return len(self.string)

    def __setitem__(self, index, value):
        self.my_list[index] = value

    def __getitem__(self, index):
        return self.my_list[index]


# Main Method
if __name__ == '__main__':
    obj = String("Rahul", [1, 2, 3, 4])
    print(obj.__doc__)                # Documentation [Doc-String]
    print(obj)                        # Printing the object into console
    print(obj + " Herooo!!")          # Adding
    print(len(obj))
    obj.__setitem__(1, 99)
    print(obj.my_list)