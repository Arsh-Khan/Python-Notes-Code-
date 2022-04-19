# greeting = "Good Morning , "
# name = "Arsh"
# c = greeting + name #Concatenating strings 
# print(c)

name = "Harry"
#print(name[0]) #for accessing individual character
# name[3]="d" --> does not work

#string slicing
# print(name[0:3]) #it will exclude 3 so it will print char at 0,1,2
# print(name[0:4])
# print(name[1:3])

# print(name[:4]) #is same as name[0:4] lowest index
# print(name[0:]) #is same as name[0:5] largest index
# print(name[1:]) #is same as name[1:5]

#negative indices
# c = name[-4:-1] #is same as name[1:4]
# print(c)

#slicing with skipping
name = "HarryIsGood"
#third value entered represents skipping value
print(name[0::1]) #skips 0 
print(name[0::2]) #skips 1
print(name[0::3])#skips 2