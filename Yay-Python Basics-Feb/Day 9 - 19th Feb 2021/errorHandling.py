# Error Handling in Python

# * Syntax Errors

'''
==> Syntax errors, also known as parsing errors, are perhaps the most common kind of complaint you get while you
are still learning Python.
'''


# * Exceptions

'''
Even if a statement or expression is syntactically correct, it may cause an error when an attempt 
is made to execute it. 
Errors detected during execution are called exceptions and are not unconditionally fatal: you will 
soon learn how to handle them in Python programs. 
Most exceptions are not handled by programs.
'''

# Handling Exceptions

## Example - 1 
# x, y = 9, 0
# try:
#     print(x / y)
# except:
#     print("Excpetion has Occured")

# except TypeError as t:
#     print(t.__class__)                 # DUNDER[Double UNDER-Score] Method to Find out the Type of Exception
#     print("TypeError has Occured!")

# except ValueError as v:
#     print(v.__class__)                 # DUNDER[Double UNDER-Score] Method to Find out the Type of Exception
#     print("ValueError has Occured!")

# except ZeroDivisionError as z:
#     print(z.__class__)
#     print("ZeroDivision has Occured!")

# except:
#     print("I don't know what kind of Excpetion is this!!")


# ## Example - 2
# x = [1, 2, 3, 4, 5, 6, "7", "a"]
# for i in x:
#     try:
#         if int(i) % 1:
#             pass
#     except Exception as e:
#         print(f"Not an Integer: {i}")
#         print(e.__class__)
# print("Nothing!")

# # ## Example - 3
# try:
#     a = int(input("Enter a Number: "))
#     if a <= 0:
#         print("Less Than 0")
# except Exception as e:
#     print(e)
#     print("Invalid Input")

# User Defined Errors Handling [Specifying the Error Message by Your Own]

# ## Example - 1
# try:
#     a = int(input("Enter a Number: "))
#     if a <= 0:
#         raise ValueError("This Value is Less than 0")
# except ValueError as ve:
#     print(ve)

# ## Example - 2
# x = 7
# try:
#     if x >= 9:
#         pass
#     else:
#         raise ValueError("Hehehahoho")
# except Exception as e:
#     print(e)

# Working with `assert`

# ## Example - 1
# try:
#     num = int(input("Enter Numerator: "))
#     deno = int(input("Enter Denominator: "))
#     assert deno != 0                             # If a Condition in `assert` is True, it'll go to `except` else not.
# except:
#     print("Denominator is Zero!!!")
# else:
#     reciprocal = 1 / num
#     print(reciprocal)

# Usage of Finally

## Example - 1
try:
    num = int(input("Enter Numerator: "))
    deno = int(input("Enter Denominator: "))
    assert deno != 0                             # If a Condition in `assert` is True, it'll go to `except` else not.
except:
    print("Denominator is Zero!!!")
else:
    reciprocal = 1 / num
    print(reciprocal)
finally:
    print("Program Execution Successful!")
# print("Program Execution Successful!")