# Importing the Necessary Class
from AbstractClassBase import Cars


# Derived Class `Benz`
class Benz(Cars):

    companyName = "Mercedes Benz"                    # Class Variable

    def __init__(self, model):
        self.modelName = model
        if model == 'GLS':
            self.price = 68000000
        else:
            self.price = 54000000

    def no_of_wheels(self):
        return f"No. of Wheels: {super().no_of_wheels()}"

    @property
    def priceOfCar(self):
        return f"Price of {self.modelName} is ${self.price}"


# Class `Tata` for Trucks
class Tata(Cars):

    @staticmethod
    def no_of_wheels():
        return f"No. of Wheels: {8}"


# Main Method
if __name__ == '__main__':

    benz = Benz("GLS")
    print(benz.no_of_wheels())
    print(benz.priceOfCar)
    print(benz.companyName)
    print(Tata.no_of_wheels())



