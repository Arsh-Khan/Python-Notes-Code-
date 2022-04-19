#program not done
# if length of both vectors are not equal then print vector length not equal
# do the checking with __len__ function

#edit : the program is completed during revision.

class Vector:
    def __init__(self,vec):
        self.vec = vec

    def __str__(self):
        str1 = ''
        index=0
        for i in self.vec:
            str1 += f" {i}a{index} +"
            index+=1

        return str1[:-1] #string slicing

    def __add__(self,vec2):
        newlist=[]
        for i in range(len(self.vec)):
            newlist.append(self.vec[i] + vec2.vec[i])    
        return Vector(newlist)
    
    def __mul__(self,vec2):
        sum = 0
        for i in range(len(self.vec)):
            sum += self.vec[i]*vec2.vec[i]    
        return sum

    def __len__(self):
        return len(self.vec)     

v1 = Vector([1,4,6])
v2 = Vector([1,6,9])

l1 = len(v1)
l2 = len(v2)

if l1==l2:
    print(v1+v2)
    print(v1*v2)
else:
    print("The given two Vectors are of different length ")