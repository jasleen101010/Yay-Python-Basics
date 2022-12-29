# What are Modules Basically?

"""
Modules are Python .py files that consist of Python code. Any Python file can be referenced as a module.
A Python file called hello.py has the module name of hello that can be imported into other Python files or used on
the Python command line interpreter.
Modules can define functions, classes, and variables that you can reference in other Python .py files or via the
Python command line interpreter.
In Python, modules are accessed by using the import statement. When you do this, you execute the code of the module,
keeping the scopes of the definitions so that your current file(s) can make use of these.
When Python imports a module called hello for example, the interpreter will first search for a built-in module
called hello.
If a built-in module is not found, the Python interpreter will then search for a file named hello.py in a list of
directories that it receives from the sys.path variable.
"""

# A Random Function
def randomFunction(x, y):
    return x + y

# Another Function
def anotherFunction(x, y):
    return x - y

# A Random Variable
randomVariable = 8

# print(randomVariable)
