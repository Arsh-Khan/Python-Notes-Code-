a = 54  # global variable
def func1():
    global a  #for changes in global variable
    print(f"Print statement 1 : {a}")
    a = 8  # local variable if global variable not used
    print(f"Print statement 2 : {a}")

func1()
print(f"Print statement 3 : {a}") #prints global variable
    