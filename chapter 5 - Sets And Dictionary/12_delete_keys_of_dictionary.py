# Given Dictionary
sampleDict = {
  "name": "Kelly",
  "age":25,
  "salary": 8000,
  "city": "New york"
  
}

# remove the keys present in the list below from the dictionary 
keysToRemove = ["name", "salary"]

del sampleDict[keysToRemove[0]]
del sampleDict[keysToRemove[1]]

print(sampleDict)