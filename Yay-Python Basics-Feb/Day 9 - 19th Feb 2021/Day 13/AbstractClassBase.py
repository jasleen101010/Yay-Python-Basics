# Importing Libraries
from abc import ABC, abstractmethod


# Defining Base Class [Abstract Class]
class Cars(ABC):

    # Abstract Method - 1
    @abstractmethod
    def no_of_wheels(self):
        return 4

    # Abstract Method - 2
    @abstractmethod
    def priceOfCar(self):
        pass

