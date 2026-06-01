class Employee:
    a = 1
    @classmethod
    def show(cls):
        print("This is a class attribute of a is {cls.a}")

e = Employee()
e.a = 45 

e.show() # This will show the value of a as 1 because class method takes the value of a from the class not from the object

