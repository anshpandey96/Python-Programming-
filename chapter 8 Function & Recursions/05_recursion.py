# factorial is a function that is defined as the product of all positive integers less than or equal to a given positive integer. It is denoted by the symbol "!" and is commonly used in mathematics and computer science.


'''
factorial (5) = 5x4x3x2x1 = 120
factorial(1) = 1x1 = 1
factorial(2) = 2x1 = 2
factorial(3) = 3x2x1 = 6

'''

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


n = int(input("Enter a number:"))
print(f"The factorial of this number is {factorial(n)}:")
