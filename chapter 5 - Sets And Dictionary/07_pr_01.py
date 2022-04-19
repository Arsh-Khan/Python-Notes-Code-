myFruits = {
     "kalingard":"watermelon",
     "kharbooja":"muskmelon",
     "seeb":"apple",
     "mosambi":"sweet lime",
     "santra" : "orange"
}

print("Options are \n",myFruits.keys())
a=input("Enter fruit name in hindi for its translation in english \n")

print("The meaning of your word is : ",myFruits.get(a))