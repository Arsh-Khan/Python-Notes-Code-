with open("Screenshot (2122).png",'rb') as f:
    text = f.read()

print(text)

with open('pict2.png','wb') as f:
    f.write(text)

