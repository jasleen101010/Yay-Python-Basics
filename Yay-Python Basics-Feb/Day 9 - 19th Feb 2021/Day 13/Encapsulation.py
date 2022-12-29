""" Definition
Encapsulation is one of the fundamental concepts in object-oriented programming (OOP).
It describes the idea of wrapping data and the methods that work on data within one unit.
This puts restrictions on accessing variables and methods directly and can prevent the accidental modification of data.
To prevent accidental change, an object’s variable can only be changed by an object’s method. Those types of variables
are known as private variable. A class is an example of encapsulation as it encapsulates all the data that is member
functions, variables, etc.
"""

"""
Consider a real-life example of encapsulation, in a company, there are different sections like the accounts section, 
finance section, sales section etc. The finance section handles all the financial transactions and keeps records of all
the data related to finance. Similarly, the sales section handles all the sales-related activities and keeps records of
all the sales. Now there may arise a situation when for some reason an official from the finance section needs all the
data about sales in a particular month. In this case, he is not allowed to directly access the data of the sales 
section. He will first have to contact some other officer in the sales section and then request him to give the 
particular data. This is what encapsulation is. Here the data of the sales section and the employees that can 
manipulate them are wrapped under a single name “sales section”. Using encapsulation also hides the data. 
In this example, the data of the sections like sales, finance, or accounts are hidden from any other section.
"""

"""
Protected members
Protected members (in C++ and JAVA) are those members of the class that cannot be accessed outside the class but can be 
accessed from within the class and its subclasses. 
To accomplish this in Python, just follow the convention by prefixing the name of the member by a single underscore “_”
or double underscore “__”.
"""


# Example 1


# # Person Class
# class Person:
#
#     def __init__(self):
#         self.name = "Rahul"
#         self.__lastName = "Bordoloi"                # Private Variable [Cannot be Accessed Outside the Class]
#
#     def printName(self):
#         return self.name + " " + self.__lastName
#
#     def displayLastName(self):
#         return self.__lastName
#
#
# # Main Method [Driver Code]
# if __name__ == '__main__':
#
#     P = Person()
#     print(P.name)
#     P.name = "Rony"
#     print(P.printName())
#     # print(P.__lastName)
#     print(P.displayLastName())


# Example 2


# # Base Class
# class Base:
#
#     def __init__(self):
#
#         # Protected Member
#         self._a = 2
#
#
# # Derived Class
# class Derived(Base):
#
#     def __init__(self):
#
#         super().__init__()
#         print("Calling Protected Method of Base Class: ")
#         print(self._a)
#
#
# # Derived Class of the Derived Class
# class anotheDerived(Derived):
#
#     def __init__(self):
#
#         super().__init__()
#         print("ANOTHER Calling Protected Member of Base Class: ")
#         print(self._a)
#
#
# # Driver Code [Main Method]
# if __name__ == '__main__':
#
#     obj = Derived()
#     obj1 = Base()
#     print(obj1._a)
#     obj3 = anotheDerived()


# Example 3


class Base:

    def __init__(self):
        self.a = "Rahul Bordoloi"
        self._b = "Rony Bordoloi"

class Derived:

    def __int__(self):
        Base.__init__()



obj = Derived()




""" Definition
Encapsulation is one of the fundamental concepts in object-oriented programming (OOP).
It describes the idea of wrapping data and the methods that work on data within one unit.
This puts restrictions on accessing variables and methods directly and can prevent the accidental modification of data.
To prevent accidental change, an object’s variable can only be changed by an object’s method. Those types of variables
are known as private variable. A class is an example of encapsulation as it encapsulates all the data that is member
functions, variables, etc.
"""

"""
Consider a real-life example of encapsulation, in a company, there are different sections like the accounts section, 
finance section, sales section etc. The finance section handles all the financial transactions and keeps records of all
the data related to finance. Similarly, the sales section handles all the sales-related activities and keeps records of
all the sales. Now there may arise a situation when for some reason an official from the finance section needs all the
data about sales in a particular month. In this case, he is not allowed to directly access the data of the sales 
section. He will first have to contact some other officer in the sales section and then request him to give the 
particular data. This is what encapsulation is. Here the data of the sales section and the employees that can 
manipulate them are wrapped under a single name “sales section”. Using encapsulation also hides the data. 
In this example, the data of the sections like sales, finance, or accounts are hidden from any other section.
"""

"""
Protected members
Protected members (in C++ and JAVA) are those members of the class that cannot be accessed outside the class but can be 
accessed from within the class and its subclasses. 
To accomplish this in Python, just follow the convention by prefixing the name of the member by a single underscore “_”
or double underscore “__”.
"""


# Example 1


# # Person Class
# class Person:
#
#     def __init__(self):
#         self.name = "Rahul"
#         self.__lastName = "Bordoloi"                # Private Variable [Cannot be Accessed Outside the Class]
#
#     def printName(self):
#         return self.name + " " + self.__lastName
#
#     def displayLastName(self):
#         return self.__lastName
#
#
# # Main Method [Driver Code]
# if __name__ == '__main__':
#
#     P = Person()
#     print(P.name)
#     P.name = "Rony"
#     print(P.printName())
#     # print(P.__lastName)
#     print(P.displayLastName())


# Example 2


# # Base Class
# class Base:
#
#     def __init__(self):
#
#         # Protected Member
#         self._a = 2
#
#
# # Derived Class
# class Derived(Base):
#
#     def __init__(self):
#
#         super().__init__()
#         print("Calling Protected Method of Base Class: ")
#         print(self._a)
#
#
# # Derived Class of the Derived Class
# class anotheDerived(Derived):
#
#     def __init__(self):
#
#         super().__init__()
#         print("ANOTHER Calling Protected Member of Base Class: ")
#         print(self._a)
#
#
# # Driver Code [Main Method]
# if __name__ == '__main__':
#
#     obj = Derived()
#     obj1 = Base()
#     print(obj1._a)
#     obj3 = anotheDerived()


# Example 3


class Base:

    def __init__(self):
        self.a = "Rahul Bordoloi"
        self._b = "Rony Bordoloi"

class Derived:

    def __int__(self):
        Base.__init__()



obj = Derived()




""" Definition
Encapsulation is one of the fundamental concepts in object-oriented programming (OOP).
It describes the idea of wrapping data and the methods that work on data within one unit.
This puts restrictions on accessing variables and methods directly and can prevent the accidental modification of data.
To prevent accidental change, an object’s variable can only be changed by an object’s method. Those types of variables
are known as private variable. A class is an example of encapsulation as it encapsulates all the data that is member
functions, variables, etc.
"""

"""
Consider a real-life example of encapsulation, in a company, there are different sections like the accounts section, 
finance section, sales section etc. The finance section handles all the financial transactions and keeps records of all
the data related to finance. Similarly, the sales section handles all the sales-related activities and keeps records of
all the sales. Now there may arise a situation when for some reason an official from the finance section needs all the
data about sales in a particular month. In this case, he is not allowed to directly access the data of the sales 
section. He will first have to contact some other officer in the sales section and then request him to give the 
particular data. This is what encapsulation is. Here the data of the sales section and the employees that can 
manipulate them are wrapped under a single name “sales section”. Using encapsulation also hides the data. 
In this example, the data of the sections like sales, finance, or accounts are hidden from any other section.
"""

"""
Protected members
Protected members (in C++ and JAVA) are those members of the class that cannot be accessed outside the class but can be 
accessed from within the class and its subclasses. 
To accomplish this in Python, just follow the convention by prefixing the name of the member by a single underscore “_”
or double underscore “__”.
"""


# Example 1


# # Person Class
# class Person:
#
#     def __init__(self):
#         self.name = "Rahul"
#         self.__lastName = "Bordoloi"                # Private Variable [Cannot be Accessed Outside the Class]
#
#     def printName(self):
#         return self.name + " " + self.__lastName
#
#     def displayLastName(self):
#         return self.__lastName
#
#
# # Main Method [Driver Code]
# if __name__ == '__main__':
#
#     P = Person()
#     print(P.name)
#     P.name = "Rony"
#     print(P.printName())
#     # print(P.__lastName)
#     print(P.displayLastName())


# Example 2


# # Base Class
# class Base:
#
#     def __init__(self):
#
#         # Protected Member
#         self._a = 2
#
#
# # Derived Class
# class Derived(Base):
#
#     def __init__(self):
#
#         super().__init__()
#         print("Calling Protected Method of Base Class: ")
#         print(self._a)
#
#
# # Derived Class of the Derived Class
# class anotheDerived(Derived):
#
#     def __init__(self):
#
#         super().__init__()
#         print("ANOTHER Calling Protected Member of Base Class: ")
#         print(self._a)
#
#
# # Driver Code [Main Method]
# if __name__ == '__main__':
#
#     obj = Derived()
#     obj1 = Base()
#     print(obj1._a)
#     obj3 = anotheDerived()


# Example 3


class Base:

    def __init__(self):
        self.a = "Rahul Bordoloi"
        self._b = "Rony Bordoloi"

class Derived:

    def __int__(self):
        Base.__init__()



obj = Derived()




""" Definition
Encapsulation is one of the fundamental concepts in object-oriented programming (OOP).
It describes the idea of wrapping data and the methods that work on data within one unit.
This puts restrictions on accessing variables and methods directly and can prevent the accidental modification of data.
To prevent accidental change, an object’s variable can only be changed by an object’s method. Those types of variables
are known as private variable. A class is an example of encapsulation as it encapsulates all the data that is member
functions, variables, etc.
"""

"""
Consider a real-life example of encapsulation, in a company, there are different sections like the accounts section, 
finance section, sales section etc. The finance section handles all the financial transactions and keeps records of all
the data related to finance. Similarly, the sales section handles all the sales-related activities and keeps records of
all the sales. Now there may arise a situation when for some reason an official from the finance section needs all the
data about sales in a particular month. In this case, he is not allowed to directly access the data of the sales 
section. He will first have to contact some other officer in the sales section and then request him to give the 
particular data. This is what encapsulation is. Here the data of the sales section and the employees that can 
manipulate them are wrapped under a single name “sales section”. Using encapsulation also hides the data. 
In this example, the data of the sections like sales, finance, or accounts are hidden from any other section.
"""

"""
Protected members
Protected members (in C++ and JAVA) are those members of the class that cannot be accessed outside the class but can be 
accessed from within the class and its subclasses. 
To accomplish this in Python, just follow the convention by prefixing the name of the member by a single underscore “_”
or double underscore “__”.
"""


# Example 1


# # Person Class
# class Person:
#
#     def __init__(self):
#         self.name = "Rahul"
#         self.__lastName = "Bordoloi"                # Private Variable [Cannot be Accessed Outside the Class]
#
#     def printName(self):
#         return self.name + " " + self.__lastName
#
#     def displayLastName(self):
#         return self.__lastName
#
#
# # Main Method [Driver Code]
# if __name__ == '__main__':
#
#     P = Person()
#     print(P.name)
#     P.name = "Rony"
#     print(P.printName())
#     # print(P.__lastName)
#     print(P.displayLastName())


# Example 2


# # Base Class
# class Base:
#
#     def __init__(self):
#
#         # Protected Member
#         self._a = 2
#
#
# # Derived Class
# class Derived(Base):
#
#     def __init__(self):
#
#         super().__init__()
#         print("Calling Protected Method of Base Class: ")
#         print(self._a)
#
#
# # Derived Class of the Derived Class
# class anotheDerived(Derived):
#
#     def __init__(self):
#
#         super().__init__()
#         print("ANOTHER Calling Protected Member of Base Class: ")
#         print(self._a)
#
#
# # Driver Code [Main Method]
# if __name__ == '__main__':
#
#     obj = Derived()
#     obj1 = Base()
#     print(obj1._a)
#     obj3 = anotheDerived()


# Example 3


class Base:

    def __init__(self):
        self.a = "Rahul Bordoloi"
        self._b = "Rony Bordoloi"

class Derived:


    def __int__(self):
        Base.__init__()



obj = Derived()




