# we can also make new file using 'w'
#f.write is used when we want to empty the file and write anthing thats inside write funcn

f = open('another.txt','w')
f.write("Please2 write to this file")
f.write("Please2 write to this file")
f.close()

f=open('another.txt','a')
f.write("I am Appending") #if you press run button multiple times it will append multiple times
f.close()
