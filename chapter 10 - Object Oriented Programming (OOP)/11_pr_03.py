# does this change the class attribute ? 
#  NO!


class Sample:
    a = "Harry"  #class attribute

obj = Sample()
obj.a = "Arsh" #instance attribute

# Sample.a = "Arsh" --> this changes class attribute

print(Sample.a) #checks for class attribute
print(obj.a) #first this checks for instance and then class attribute

Sample.a = "dubai"
print(Sample.a)
print(obj.a)
