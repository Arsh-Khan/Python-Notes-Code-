class Employee:
    company="Google"
    def getsalary(self,signature): #if self is absent error--->gettsalary() takes 0 positional arguments but 1 was given
        print(f"Salary for this Employee working in {self.company} is {self.salary} \n{signature}")
    
    @staticmethod  #decorator
    def greet():
        print("Good Morning , Sir")

    @staticmethod
    def time():
        print("The time is 9AM")    

harry = Employee()
harry.salary = 100000
harry.getsalary("Thanks!")
# Employee.getSalary(harry) the above line gets converted to this line
harry.greet()
harry.time()     