class Employee:
    company = "Camel"
    salary = 100
    location = "delhi"

    def changeSalary(self,sal):  # instance attribue of e , it dosent change the value of class attribute
        self.salary = sal        #class attribute does not change

    # def changeSalary2(self,sal): 
    #     self.__class__.salary = sal   #it changes class attribute
    #     #__class__ is called dunder class
    
    @classmethod                  # another statements for doing above job
    def changeSalary2(cls,sal): 
        cls.salary = sal 
        
e = Employee()

print(e.salary)
e.changeSalary2(455) 
print(e.salary)
print(Employee.salary) 


