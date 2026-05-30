class Employee:
    language = "python"
    salary = 100000

    def __init__(self): # dunder methon which is automatically call 
         print("I am creating an object")

    def getInfo(self, name,salary,language):
            self.name = name 
            self.salary = salary
            self.language = language

    def showInfo(self):
        print(f"The language is {self.language}.The salary is {self.salary}.The name is {self.name}.")



    @staticmethod
    def greet():
            print("Good Morning")


ansh = Employee()
ansh.getInfo("ansh", 13000000, "Javascript") # this is an instance 
print(ansh.name,ansh.salary,ansh.language)

#rohan = Employee()

