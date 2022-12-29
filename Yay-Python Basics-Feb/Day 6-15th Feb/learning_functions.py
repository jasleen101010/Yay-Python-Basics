def my_first_function():
    print("I love Batman")


my_first_function()


def square(x, y):
    print(x * y)
    print(x - y)


square(10, 2)


def sayhello(*names):
    for name in names:
        print(f'Hello {name}')


sayhello('Jasleen', 'Abhijit', 'Abhilipsa','Ritika')

def multiply(a,b):
    return a*b
multiply(2,3)

for i in zip([1,2,3],['a','b','c']):
        print(i)
a = ("John", "Charles", "Mike")
b = ("Jenny", "Christy", "Monica", "Vicky")

x = zip(a, b)
print(x)
print(list(x))



