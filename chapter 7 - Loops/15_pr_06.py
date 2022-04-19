n = int(input("Enter a Number : "))
fact = 1

for i in range(1,n+1):
    fact=fact*i

print(f"The factorial of {n} is : {fact}")