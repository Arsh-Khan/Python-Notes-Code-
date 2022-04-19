
class Employee:
    company="Google"
    def getsalary(self): #if self is absent error--->gettsalary() takes 0 positional arguments but 1 was given
        print(f"Salary for this Employee working in {self.company} is {self.salary}")

harry = Employee()
harry.salary = 100000


harry.getsalary()
# Employee.getSalary(harry) the above line gets converted to this line
     