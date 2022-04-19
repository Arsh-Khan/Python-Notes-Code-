with open('poem.txt','r') as f:
    a = f.read()

if "twinkle" in a:
    print("Twinkle is present")
else:
    print("Twinkle is not present")

                  # or
# b = a.find('twinkle')
# if(b==-1):
#     print("Word not there in file")
# else:
#     print("Word is there in file")    