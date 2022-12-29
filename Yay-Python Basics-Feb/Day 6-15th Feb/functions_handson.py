# Function FizzBuzz
def fizz_buzz(n):
    if n % 3 == 0 and n % 5 == 0:
        print('FizzBuzz')
    elif n % 3 == 0:
        print('Fizz')
    elif n % 5 == 0:
        print('Buzz')
    else:
        print(n)
# Main Method
if __name__ == '__main__':
    num=int(input("Enter the number:"))
    fizz_buzz(num)