def multiplication_table(n):
    for i in range(1,11):
        print(f"{n} X {i} = {n*i}")

n=int(input("Enter the number : "))
multiplication_table(n)
