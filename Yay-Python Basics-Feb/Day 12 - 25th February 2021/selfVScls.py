# Class `Explainatin`
class Explaination:

    class_variable = "Rahul Bordoloi"

    def __init__(self, name):
        self.name = name

    def thisIsAInstanceMethod(self):
        print(self.name)

    @classmethod
    def thisIsAClassMethod(cls):
        print(cls.class_variable)


# Main Method
if __name__ == '__main__':
    obj = Explaination('Alex')
    obj.thisIsAInstanceMethod()
    obj.thisIsAClassMethod()
    print(dir(obj))                     # Used to Get Names of all the Methods and Variables associated with that Object

