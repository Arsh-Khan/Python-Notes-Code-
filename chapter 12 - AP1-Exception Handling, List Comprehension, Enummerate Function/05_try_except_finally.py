try:
    i = int(input("Enter a number : "))
    c = 1/i
except Exception as e:
    print(e)
    exit()
finally:    #even if program is ending in exit() still code inside finally will run , this makes it different from writting the code without finally
    print("We were Done") 

print("Thanks for using the program")