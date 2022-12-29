# Python code to illustrate cube of a number
# showing difference between def() and lambda().
def cube(y):
    return y * y * y


lambda_cube = lambda y: y * y * y

# using the normally
# defined function
print(cube(5))

# using the lamda function
print(lambda_cube(5))