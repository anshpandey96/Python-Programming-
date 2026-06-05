# Map Example 

l = [1,2,3,4,5]

square = lambda x: x*x

sqList  = map(square , l)

print(list(sqList))


# Filter Example
def even(n):
    return n % 2 == 0

onlyEven = filter(even, l)
print(list(onlyEven))


# reduce Example
from functools import reduce

def sum(a, b):
    return a + b

mul = lambda x,y:x*y

total = reduce(sum, l)
print(reduce(mul, l))
print(total)
