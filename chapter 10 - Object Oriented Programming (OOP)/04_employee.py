# Class Attributes

class Employee:
    company="Google"

harry = Employee()
arsh = Employee()

print(harry.company)
print(arsh.company)

Employee.company = "Youtube" #changing class attribute

print(harry.company)
print(arsh.company)

