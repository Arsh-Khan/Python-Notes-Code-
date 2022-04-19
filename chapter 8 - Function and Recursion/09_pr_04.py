def sum_recursive(n):
   if n==1:
       return 1 

   return n + sum_recursive(n-1)

n=int(input("Enter the nth term : "))
sum=sum_recursive(n)
print(f"The sum of n natural nos is {sum}")
