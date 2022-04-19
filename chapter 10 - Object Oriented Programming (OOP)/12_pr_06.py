class Sample:
    def __init__(slf,name): #we can write anything in place of self but for readability(when others use our code) of the code we use self
        slf.name = name 

obj = Sample("Harry")
print(obj.name)