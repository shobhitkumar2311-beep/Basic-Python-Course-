# Create a class “Programmer” for storing information of few programmers working at Microsoft.

# Creating the class
class programmer:

    #Given some value as the starting
    company = "Microsoft"
    pin = 245001

    # Creating the function for the opration
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

# Taking information of worker.
p = programmer("Harry", 120000)
print(p.name, p.salary, p.pin, p.company)

r = programmer("Rohan", 150000)
print(r.name, r.salary, r.pin, r.company)













