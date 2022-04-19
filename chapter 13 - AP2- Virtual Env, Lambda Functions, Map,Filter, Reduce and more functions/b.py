
def funcn():
    n,k=input("").split()
    n = int(n)
    k = int(k)
    l1=[]
    
    l =[j for j in range(1,n,2)]
    for j in range (2,n+1,2):
        l.append(j) 
    
    for j in range(1,k):
        for m in range(0,len(l),2):
            l1.append(l[m])
     
        for m in range(1,n):
            if l[m] in l1:
                continue
            else:
                l1.append(l[m])
        if j!=k-1:
            l=l1
            l1=[]

    for item in l1:
        print(item,end=" ")
    

t = int(input(""))
for i in range(t):
     funcn()       





    
    