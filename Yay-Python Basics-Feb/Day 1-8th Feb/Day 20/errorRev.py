# print("Hello World")
# for i in range(10):
#     print(i)

try:
    print(8 / 0)

except ValueError as e:
    print(e.__class__)
    print("Exception has Occured")

except ZeroDivisionError as e:
    print(e.__class__)
    print("Exception has Occured")

print("Finally!!")
