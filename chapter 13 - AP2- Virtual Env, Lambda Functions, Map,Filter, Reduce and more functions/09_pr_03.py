n = int(input("Enter a Number : "))
table = [str(n*i) for i in range(1,11)]

verticalTable = "\n".join(table) 
print(verticalTable)


