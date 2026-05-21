a = int(input("Enter a first number : "))
b = int(input("Enter a second number : "))
c = int(input("Enter a third number : "))
d = int(input("Enter a fourth number : "))

if (a > b and a > c and a > d):
    print("A is the greatest number", a)

elif b > a and b > c and b > d:
    print("B is the greatest number", b)

elif c > a and c > b and c > d:
    print("C is the greatest number", c)

elif d > a and d > b and d > c:
    print("D is the greatest number", d)

