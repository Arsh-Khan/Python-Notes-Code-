n = int(input("Enter a Number : "))
count=0
for i in range(2,n):
    if(n%i==0):
        count=count+1
        break

if count==1:
    print("Not a Prime No")
else:
    print("A Prime No")            