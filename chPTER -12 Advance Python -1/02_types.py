from typing import List, Union, Tuple, Dict

# List of Integers
numbers: List[int] = [1, 2, 3, 4, 5]
n: int = 5

# Tuple of a string and an integer
person: Tuple[str, int] = ("Alice", 90)

# Dictionary of string keys and int values
scores: Dict[str, int] = {"Alice": 90, "Bob": 85}

# Union type for variable that can hold multiple types
identifier: Union[int, str] = "ID123"
identifier = 12345  # also valid

# Example function with type hints
def sum(a: int, b: int) -> int:
    return a + b

print(numbers)       # [1, 2, 3, 4, 5]
print(n)             # 5
print(person)        # ('Alice', 90)
print(scores)        # {'Alice': 90, 'Bob': 85}
print(identifier)    # 12345
print(sum(10, 20))   # 30
