class Employee:
    company = "Google"
    
    def showDetails(self):
        print("This is an Employee")

class Programmer(Employee):
    language = 'Python'
    # company = 'Youtube' 
    def getLanguage(self):
        print(f"The language is : {self.language}")
    
    # def showDetails(self):
    #     print("This is an Programmer")

e = Employee()
e.showDetails()
p = Programmer()
p.showDetails() #if showDetails is not in programmer class than it will print showdetails of base class through inheritance (overwrites it)
print(p.company) #Same for this also
# e.getLanguage()--->gives an error