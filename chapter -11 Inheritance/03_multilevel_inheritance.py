class Employee:
     a = 1


class Programmer(Employee):

      b = 2

class Manager(Programmer):
     
     c  = 3

o = Employee()
print(o.a)
# print(o.b)

o = Programmer()
print(o.a,o.b) # Shows an error becsue there is no b attribute in Employee class

O = Manager()
print(O.a,O.b,O.c) # Shows all attributes from the inheritance chain

