# `Pet` Class - Parent Class
class Pet:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show(self):
        print(f"I'm {self.name} and I'm {self.age} years old!")

    def speak(self):
        print("I don't know what do I say here!")


# `Cat` Class - Child Class
class Cat(Pet):

    def __init__(self, name, age, colour):
        super().__init__(name, age)
        self.colour = colour

    def speak(self):
        print("Meow")

    def show(self):
        print(f"I'm {self.name} and I'm {self.age} years old and I'm {self.colour} in Colour!!")


# `Dog` Class - Child Class
class Dog(Pet):

    def __init__(self, name, age, colour):
        super().__init__(name, age)
        self.colour = colour

    def speak(self):
        print("Bark")

    def show(self):
        print(f"I'm {self.name} and I'm {self.age} years old and I'm {self.colour} in Colour!!")


# `Fish` Class - Child Class
class Fish(Pet):
    pass


# Main Method
if __name__ == '__main__':

    pet = Pet("Don", 12)
    pet.show()
    pet.speak()
    cat = Cat("Meowski", 6, "White")
    cat.speak()
    cat.show()
    dog = Dog("Doniski", 8, "Brown")
    dog.speak()
    dog.show()
    fish = Fish("Bubbles", 2)
    fish.show()
    fish.speak()