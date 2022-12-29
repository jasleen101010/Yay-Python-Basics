# Class `Math`
class Math:

    # Static Method - 1
    @staticmethod
    def add5(x):
        return x + 5

    # Static Method - 2
    @staticmethod
    def multiply5(x):
        return x * 5

    # Static Method - 3
    @staticmethod
    def printRun():
        print("Run!")


# Main Method
if __name__ == '__main__':
    print(Math.add5(10))
    print(Math.multiply5(20))
    Math.printRun()



