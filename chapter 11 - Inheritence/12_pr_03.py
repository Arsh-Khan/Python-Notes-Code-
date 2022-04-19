# salaryAfterIncrement = salary * increment

class Emloyee:
    salary = 1000
    increment = 1.5

    @property
    def salaryAfterIncrement(self):
        return self.salary * self.increment

    @salaryAfterIncrement.setter
    def salaryAfterIncrement(self,sai):
        self.increment = sai/self.salary

e = Emloyee() 
print(e.salaryAfterIncrement)
print(e.increment)

e.salaryAfterIncrement = 2000
print(e.increment)

    