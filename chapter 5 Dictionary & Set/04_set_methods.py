s = { 5,7,47,32,1,66,2,"Ansh" } # repation is not allowed in set
print(s, type(s))

# s.add(566(s))

s.add(566)
print(s, type(s))

s.remove(5)


# Must Know 
len([1,2,3])           # 3       — length
type("hello")          # <str>   — type check
print("Hello")         # output
input("Name: ")        # user se input lo
range(1, 6)            # 1,2,3,4,5

# Type Convert
int("42")              # 42
float("3.14")          # 3.14
str(100)               # "100"
list((1,2,3))          # [1,2,3]

# Math
abs(-10)               # 10
max(1,2,3)             # 3
min(1,2,3)             # 1
sum([1,2,3])           # 6
round(3.567, 2)        # 3.57
pow(2, 8)              # 256

# Super Useful
sorted([3,1,2])        # [1,2,3]
reversed([1,2,3])      # [3,2,1]
enumerate(["a","b"])   # (0,'a'),(1,'b')
zip([1,2],[3,4])       # (1,3),(2,4)
map(str, [1,2,3])      # ['1','2','3']
filter(lambda x: x>2, [1,2,3,4])  # [3,4]

# Object Info
dir("hello")           # saare methods dekho
help(list.append)      # documentation
isinstance(5, int)     # True

