class Employee:
    company = "Google"
    name = "default name"
    salary = 10000
    def show (self):
        print(f"The name of the Employee is { self.name} and the salary is {self.salary}")

class coder:
    language = "python"
    def showlanguage(self):
        print(f"Out of all the language here is your language here is your language {self.language}")


class Programmer(Employee,coder):
    company = "Microsoft"
    def showlanguage(self):
        print(f"The name is { self.company} and the language is {self.language}")

a = Employee()
b = Programmer()

b.show()
b.showlanguage()
b.showlanguage()
