def pattern(n):
    for i in range (n,0,-1):
        print("*"*i)

        # or
    # for i in range(n):
    #     print("*"*(n-i))   

n=int(input("Enter the nth term : "))
pattern(n)