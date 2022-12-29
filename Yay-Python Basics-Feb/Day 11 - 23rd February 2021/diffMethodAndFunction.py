# This is a Function
def sumF(x, y):
    return x + y

# This is a Class
class sum:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    # This is a Method
    def sumF(self):
        return self.x + self.y


# This is a Function
print("Function: ", sumF(7, 8))

# This is a Methpd
print("Method: ", sum(7, 8).sumF())

