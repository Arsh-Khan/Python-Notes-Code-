#correction in question,its not list its string

def remove_and_strip(word,string):
    newStr=string.replace(word, "")
    return newStr.strip()

this = "      Harry is a good   "
n=remove_and_strip("Harry",this)
print(n)
