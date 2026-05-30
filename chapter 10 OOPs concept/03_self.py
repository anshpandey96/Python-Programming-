class Employee:
    language = "python"
    salary = 100000

    def getInfo(self):
        print(f"The language is {self.language}.The salary is {self.salary}.")
    @staticmethod
    def greet():
            print("Good Morning")


ansh = Employee()
ansh.language = "javascript" # this is an instance attribute 

ansh.getInfo() # this will give an error as getInfo is a class method and we are trying to access it through an instance . we can only access class attributes through class methods and instance attributes through instance methods .
# Employee.getInfo(ansh) # this will work as getInfo is a class method and we are trying to access it through the class . we can only access class attributes through class methods and instance attributes through instance methods .
