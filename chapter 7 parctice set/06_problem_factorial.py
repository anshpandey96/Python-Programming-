# 5! = 1x 2x3x4xx5x6

n = int(input("Enter the number :"))
product = 1
for i in range(1, n+1):
    product = product * i 

print(f"The factorial of {n} is {product}")    