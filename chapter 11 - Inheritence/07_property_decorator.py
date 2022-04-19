class Employee:
    company = "Bharat Gas"
    salary = 5600
    salarybonus = 400

    # totalSalaryBonus = 6100 -->agar apne ko salary and salarybonus mai kuch change karna ho toh uski value update nahi kar sakte
    
    @property
    def totalSalary(self):
        return self.salary + self.salarybonus

    @totalSalary.setter
    def totalSalary(self,val):
        self.salarybonus = val - self.salary    

e = Employee()
print(e.totalSalary)

e.totalSalary = 5800  #ye setter run karwayega

print(e.salary)
print(e.salarybonus)
# functions mai () use karte hai
# properties main bracket nahi use karte hai
