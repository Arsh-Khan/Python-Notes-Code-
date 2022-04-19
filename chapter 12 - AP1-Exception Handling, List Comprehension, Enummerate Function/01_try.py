while(True):
    print("Press q to quit")
    a = input("Enter a Number : ")

    if a=='q':
        break
    
    try:
        print("Trying .....")
        a = int(a)
        if a>6:
            print("Number entered is greater than 6")
    except Exception as e:
        print(f"Your input resulted in an error : {e}")


print("Thanks for playing this game")