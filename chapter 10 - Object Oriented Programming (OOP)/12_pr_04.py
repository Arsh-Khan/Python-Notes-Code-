class Calculator:
    def __init__(self,num):
        self.num=num
    
    def squareRoot(self):
        print(f"Square Root of Entered no {self.num} is :{self.num**0.5}")
    
    def square(self):
        print(f"Square of Entered no {self.num} is :{self.num **2}")
    
    def cube(self):
        print(f"Cube of Entered no {self.num} is :{self.num **3}")

    @staticmethod
    def greet():
        print("******** Hello there welcome to the best Calculator of the world ********")    

n = Calculator(9)
n.greet()
n.squareRoot()
n.square()
n.cube()

