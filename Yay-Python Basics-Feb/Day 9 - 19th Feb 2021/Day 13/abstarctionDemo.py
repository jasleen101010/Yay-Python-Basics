# Abstract Class [Interface]
class myInfo:

    def getName(self):
        pass

    def setName(self):
        pass


# `Rahul` Class
class Rahul(myInfo):

    def __init__(self):
        self.name = None

    def setName(self):
        self.name = input("Enter your Name: ")

    def getName(self):
        return self.name


# Main Method
if __name__ == '__main__':
    obj = Rahul()
    obj.setName()
    print(obj.getName())
