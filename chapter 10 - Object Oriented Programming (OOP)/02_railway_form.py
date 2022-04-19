
class RailwayForm:
    formType = "Railway Form"
    def printData(self):
        print(f"Name of passanger : {self.name}")
        print(f"Name of Train : {self.train}")

harrysApplication = RailwayForm()
harrysApplication.name = "Harry"
harrysApplication.train = "Rajdhani"
harrysApplication.printData()