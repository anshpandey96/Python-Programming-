class Employee:
    def __init__(self):
      print("Canstructor of Employee class")
    a = 1

class Programmer(Employee):
      
    def __init__(self):
      print("Canstruct of Programmer")
      b = 2

class Manager(Programmer):
    def __init__(self):
      print("Canstructor of Manager")
      b  = 3

o = Employee()
print(o.a)
# print(o.b)

o = Programmer()
def __init__(self):
      super().__init__() # This will call the constructor of Employee class
      print("Canstruct of Manager")
      b = 2
# print(o.a,o.b) # Shows an error becsue there is b attribute in Employee class

# O = Manager()
# def __init__(self):
#       print("Canstructor of Manager")
#       c  = 3

# o = Manager()
# print(o.a,o.b,o.c)

