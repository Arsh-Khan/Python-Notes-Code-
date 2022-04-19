
def greatest_no(n1,n2,n3):
    if(n1>n2):
        f1=n1
    else :
        f1=n2
    if(n3>f1):
        return n3
    else :
        return f1            

n1=int(input("Enter a Number 1 : "))
n2=int(input("Enter a Number 2 : "))
n3=int(input("Enter a Number 3 : "))

greatest=greatest_no(n1,n2,n3)


print(f"The greatest number among the three nos is : {greatest}")


                #  or
# def maximum(n1,n2,n3):
#     if(n1>n2):
#         if(n1>n3):
#             return n1
#         else:
#             return n3    
#     else:
#             if(n2>n3):
#             return n2
#         else:
#             return n3    
  