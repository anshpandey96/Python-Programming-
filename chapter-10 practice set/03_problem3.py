class Demo:
    a = 4

o = Demo()    
print(o.a) # Prints the class attribute because instance attributr is not present
o.a = 0  # Instance attribute is set
print(o.a) # Prints the instance attribute because it is present
print(Demo.a) #Print the class attribute because instance attribute is not present in class

