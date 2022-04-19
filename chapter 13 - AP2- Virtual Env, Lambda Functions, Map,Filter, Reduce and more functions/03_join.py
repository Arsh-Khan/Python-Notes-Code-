l = ["camera" , "Laptop" , "phone" , "ipad" , "hard disk" , "nvidia 3080 graphics card"]

# sentence = " and ".join(l)     #and will get joined after each element except last one
sentence = " \n ".join(l)     #like two elements ke beech me ye sepeartor ki tarah
print(sentence)
print(type(sentence))

##join operator can be used for any iterable objects like lists,tuples