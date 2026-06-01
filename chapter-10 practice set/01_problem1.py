class Programmer:
    company = "Microsoft"
    def __init__(self, name, salary, pin):
        self.name = name
        self.salary = salary
        self.pin = pin



p = Programmer("Ansh",120000,345001)
print(p.name, p.salary, p.pin) 
r = Programmer("Rohan",120000,3422001)
print(r.name, r.salary, r.pin, r.company)

