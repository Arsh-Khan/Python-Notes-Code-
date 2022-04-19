class Employee:
    company = "Visa"
    eCode = 120

class Freelancer:
    company = "Fiverr"
    level = 0
    def upgradeLevel(self):
        self.level = self.level + 1

class Programmer(Freelancer,Employee):
    name = 'Rohit'

p = Programmer()
p.upgradeLevel()

print(p.level)

print(p.company) #Fiveer gets printed because freelancer is written first in class programmer [line 11]