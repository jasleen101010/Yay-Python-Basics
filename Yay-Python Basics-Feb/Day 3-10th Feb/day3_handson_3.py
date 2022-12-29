arr = list(map(int, input('Enter your List : ').split()))

'''
# Method 1 - Inbuilt Function of Python
maxElement = max(arr)
'''

# Method 2
maxElement = arr[0]
for i in arr:
    if maxElement < i:
        maxElement = i

print(f'Max Element is : {maxElement}')