class Employee:
    company = "Google"
    def show (self):
        print(f"The name is { self.name} and the salary is {self.salary}")

# class Programmer(Employee):
#     company = "Microsoft"
#     def show(self):
#         print(f"The name is { self.name} and the salary is {self.salary}")

#     def showLanguage(self):
#         print(f"The name is {self.name} and the language is {self.language}")
class Programmer(Employee):
    company = "Microsoft"
    def showlanguage(self):
        print(f"The name is { self.name} and the language is {self.language}")



a = Employee()
b = Programmer()

print(a.company, b.company)

