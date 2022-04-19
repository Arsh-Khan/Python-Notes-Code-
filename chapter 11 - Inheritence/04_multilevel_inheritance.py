class Person:
    country = 'India'
    def takeBreath(self):
        print("I am breathing...")
        
class Employee(Person):
    company = 'Honda'
    def getSalary(self):
        print(f"Salary is {self.salary}")
    
    def takeBreath(self):
        print("I am an Employee , So I am luckily breathing...")

class Programmer(Employee):
    company = "Fiverr"

    def getSalary(self):
        print("No salary for programmers")

    def takeBreath(self):
        print("I am an Programmer , So I am breathing ++...")    

p = Person()
p.takeBreath()

e = Employee()
e.takeBreath()
print(e.company)

pr = Programmer()
pr.takeBreath() #Uses the latest one (nearest parent) .if theyy have their own then they will use their and if they dont they will use then nearest parent one
print(pr.company)
print(pr.country)