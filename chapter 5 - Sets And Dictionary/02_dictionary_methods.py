myDict = {
        "Fast":"In a quick manner",
        "Arsh":"A Coder",
        "Marks":[1,2,5],
        "anotherDict":{'arsh':'player'},
        1 : 2
}

print(myDict.keys())            #prints the keys of dictionary
print(type(myDict.keys()))
print(list(myDict.keys()))    #type casting
print(myDict.values())          #prints the value of dictionary
print(myDict.items())       #prints the (key,value) for all contents of dictionary in tuple form

# print(myDict)
updateDict = {
            "Lovish":"Friend", 
            "Faaiz":"Friend",
            "Arsh":"Singer"  #this also gets update 
}
myDict.update(updateDict)   # updates the dictionary by adding the key:value pair from updateDict
print(myDict)

print(myDict.get("Arsh"))  #print value associated with key "Arsh"
print(myDict["Arsh"])      #print value associated with key "Arsh".both does same job

#difference between .get and [] syntax in dictionaries

print(myDict.get("Arsh2")) # Returns none as Arsh2 is not present in the dictionary
# print(myDict["Arsh2"])     #throws an error as Arsh2 is not present in the dictionary
