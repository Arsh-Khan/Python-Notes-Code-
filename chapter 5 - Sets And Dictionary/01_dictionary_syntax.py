myDict = {
        "Fast":"In a quick manner",
        "Arsh":"A Coder",
        "Marks":[1,2,5],
        "anotherDict":{'arsh':'player'}
}
# print(myDict)
print(myDict['Fast'])
print(myDict['Arsh'])

myDict["Marks"]=[45,69] #it is mutable
print(myDict['Marks'])
print(myDict["anotherDict"])
print(myDict["anotherDict"]['arsh'])
