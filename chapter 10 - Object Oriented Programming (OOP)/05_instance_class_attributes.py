class Employee:
    company="Google"
    salary=100

harry = Employee()
arsh = Employee()

print(harry.salary)
print(arsh.salary)

# creating instance class attribute salary for both the objects

harry.salary=400
arsh.salary=500

print(harry.salary)
print(arsh.salary)

# below line throws an error as adress is not present in instance/class
# print(arsh.address) ---> throws an error employee has no attribute 'address'
