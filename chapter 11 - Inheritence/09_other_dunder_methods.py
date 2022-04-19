class Number:
    def __init__(self,num):
        self.num = num

    def __add__(self,num2):           
        print("Lets add")
        return self.num + num2.num
    
    def __mul__(self,num2):           
        print("Lets Multiply")
        return self.num * num2.num

    def __str__(self):   #this gets executed when you want to directly rint the object
        return f"Decimal no : {self.num}"

    def __len__(self):  #used for giving dimension of vector
        return 1     

n = Number(9)
print(n)
print(len(n))