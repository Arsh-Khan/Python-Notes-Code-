class Employee:
    company="Google"

    def __init__(self,name,salary,subunit): # (special function) this function runs without even calling it
        self.name = name
        self.salary = salary
        self.subunit = subunit
        print("Employee is Created!")

    def getdetails(self):
        print(f"The Name of employee is {self.name}")
        print(f"The Salary of employee is {self.salary}")
        print(f"The Subunit of employee is {self.subunit}")


    def getsalary(self,signature):
        print(f"Salary for this Employee working in {self.company} is {self.salary} \n{signature}")
    
    @staticmethod 
    def greet():
        print("Good Morning , Sir")

    @staticmethod
    def time():
        print("The time is 9AM")    

harry = Employee("Harry",100,"Youtube")
# harry = Employee() ----> this throws an error
harry.getdetails()