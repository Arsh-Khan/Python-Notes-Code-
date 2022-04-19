m1 = int(input("Enter marks of subject 1 "))
m2 = int(input("Enter marks of subject 2 "))
m3 = int(input("Enter marks of subject 3 "))

totalp = (m1+m2+m3/3)

if(m1>33 and m2>33 and m3>33 and totalp>40):
    print("Pass")
else:
    print("Fail")    



