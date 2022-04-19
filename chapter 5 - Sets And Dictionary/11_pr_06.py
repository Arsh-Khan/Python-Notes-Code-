from abc import abstractclassmethod


myDic = {}

name1=input("Enter Name 1\n")
lang1=input("Enter Favorite Language\n")
name2=input("Enter Name 2\n")
lang2=input("Enter Favorite Language\n")
name3=input("Enter Name 3\n")
lang3=input("Enter Favorite Language\n")
name4=input("Enter Name 4\n")
lang4=input("Enter Favorite Language\n")

# UpdatemyDic = {
#             name1:lang1,                  
#             name2:lang2,                  
#             name3:lang3,                  
#             name4:lang4                  
# }
# myDic.update(UpdatemyDic)
#print(myDic)
#          or (more correct)

myDic[name1]=lang1
myDic[name2]=lang2
myDic[name3]=lang3
myDic[name4]=lang4

print(myDic.keys)
