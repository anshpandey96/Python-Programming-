marks = { 
           "Ansh": 100, "Ron": 
          67, "Hermione": 13, 
           0: "Ansh" }


# print(marks.items())
# print(marks.keys())
# print(marks.values())
# marks.update({"Ansh": 99, "Ron": 68})
# print(marks)

print(marks.get("Ansh")) # prints None 
print(marks.get("Ansh")) # Returns an error because "Ansh" is not a key in the dictionary



d = {"name": "Rahul", "age": 25, "city": "Lucknow"}

# Accessing
print(d.get("name"))           # Rahul
print(d.get("salary", 0))      # 0 (default)

# Keys, Values, Items
print(d.keys())                # dict_keys(['name', 'age', 'city'])
print(d.values())              # dict_values(['Rahul', 25, 'Lucknow'])
print(d.items())               # dict_items([('name', 'Rahul'), ...])

# Update
d.update({"age": 26, "job": "Dev"})

# setdefault
d.setdefault("country", "India")   # Adds only if key missing

# pop
d.pop("city")                  # Removes 'city'

# copy
d2 = d.copy()

# fromkeys
empty = dict.fromkeys(["a", "b", "c"], 0)  # {'a': 0, 'b': 0, 'c': 0}

# clear
d.clear()                 # {}


