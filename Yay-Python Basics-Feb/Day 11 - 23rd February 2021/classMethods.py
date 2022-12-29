# Class `Person`
class Person:

    """docstring
    Just a Random Class for Tutorial
    """

    # Class Variables
    number_of_people = 0
    GRAVITY = 9.8

    # Constructor
    def __init__(self, name):

        self.name = name
        Person.addPerson()

    # Class Method - 1
    @classmethod
    def addPerson(cls):

        cls.number_of_people += 1

    # Class Method - 2
    @classmethod
    def displayNoOfPeople(cls):

        return cls.number_of_people


# Main Method
if __name__ == '__main__':

    p1 = Person("Tim")
    print(Person.number_of_people)
    p2 = Person("Ross")
    print(Person.displayNoOfPeople())



