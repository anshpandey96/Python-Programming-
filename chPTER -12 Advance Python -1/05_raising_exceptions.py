a = int(input("Enter a number : "))
b = int(input("Enter a secon number : "))

if(b == 0):
    raise ZeroDivisionError("hey our program is not meant to divide numbers by zero")

else:
    print(f"The division a/b {a/b}")