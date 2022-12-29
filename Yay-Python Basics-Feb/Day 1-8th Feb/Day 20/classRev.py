class Human:
    
    species = "Homo-Sapiens"

    # Constructor - Helps in Initialising the Class in the Memory and also to initialize Instance Variables
    def __init__(self, x, y):
        
        self.x = x
        self.y = y

    def abc(self, x):
        print(self.x + self.y + x)

    @staticmethod
    def add5(x):
        return x + 5


# obj = Human(7, 9)
# # obj.abc(9)
# print(obj.add5(9))


class HumanReDefined:

    species = "Homo-Sapiens"

    def __init__(self, name):
        self.name = name

    def getName(self):
        pass

    def setName(self):
        pass

class Boy(HumanReDefined):

    def __init__(self, name):
        super().__init__(name)

    def getName(self):
        return self.name

    def setName(self, newName):
        self.name = newName
