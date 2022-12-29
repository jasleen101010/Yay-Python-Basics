# Returning Multiple Values from a Single Function.

# Goal
'''
return:
    a + b
    a - b
    a * b * c
'''

## Function
def doSomething(a, b, c = 1):
    return a + b, a - b, a * b * c
    
## Driver Code
result_1, result_2, result_3  = doSomething(7, 8, 9)
storingInSingleVariable = doSomething(7, 8, 9)
print("Multiple Variables: ", result_1, result_2, result_3)
print(f"Storing in Single Variable: {storingInSingleVariable}, {type(storingInSingleVariable)}")
print(f"Some Operation's Result: {result_1 + result_2 + result_3}")