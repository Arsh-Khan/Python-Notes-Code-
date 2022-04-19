def greet(name):
    print(f"Good Morning , {name}")

# print(__name__)
if __name__ == '__main__':
    n = input("Enter Your Name : ")
    greet(n)
    print(__name__)


# if this code is running here it will show __name__ = __main__
# if this code is running on another file like in this case in m07.fil2 then here it will show __name__ = m06.file1
