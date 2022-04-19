num1 = int(input("Enter number 1 \n"))
num2 = int(input("Enter number 2 \n"))
num3 = int(input("Enter number 3 \n"))
num4 = int(input("Enter number 4 \n"))

if(num1>num4):
    f1=num1
else:
    f1=num4

if(num2>num3):
    f2=num2
else:
    f2=num3

if(f1>f2):
    print(str(f1) + " is greatest ")
else:
    print(str(f2) + " is greatest ")


    #traditional way

# print("The greatest number among the four numbers is : ")
# if(num1>num2 and num1>num3 and num1>num4):
#     print(num1)
# elif(num2>num1 and num2>num3 and num2>num4):
#     print(num2)
# elif(num3>num2 and num3>num1 and num3>num4):
#     print(num1)
# elif(num4>num2 and num4>num3 and num4>num1):
#     print(num4)
    
