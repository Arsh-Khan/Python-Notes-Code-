
def percent(marks):
    p = (sum(marks)/400)*100
    return p

marks = [45 , 78, 86, 77]
percentage = percent(marks) 

marks2 = [75 , 98, 88, 78]
percentage2= percent(marks2)

print(percentage,percentage2)


def mySum(num1,num2):
    return num1 + num2

s = mySum(6,32)
print(s)    