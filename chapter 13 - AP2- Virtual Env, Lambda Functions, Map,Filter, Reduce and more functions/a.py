t = int(input(""))

for i in range(t):
    s = input()
    subs=[]
    count = 0
    for j in range(0,len(s)):         
        for k in range(len(s),j,-1) :        
            subs.append(s[j:k])              

    for item in subs:
        sum = 0
         
        if int(item)==0 or int(item)==1:
            break
        cc=1
        item1 =int(item)
        while item1!=0:
            sum = sum + (item1%10)*(2**cc)
            item1=item1/10
            cc+=1
            
        for l in range(2,int(sum)):
            if int(sum)%l==0 :
                break
        else:
            count+=1
                    
    if count>0:
        print("Yes")

    else:
        print("No")        



        # for l in range(len(item)):
        #     sum = sum + int(item[l])
        

            