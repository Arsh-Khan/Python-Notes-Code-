letter = '''Dear <|Name|>
Greeting from ABC Coding house . I am happy to tell you about your selection.
You are Selected!
Have a great day ahead!
Thanks and Regards
Bill
Date : <|Date|>'''

name = input("Enter Your Name\n")
date = input("Enter the date\n")

letter = letter.replace("<|Name|>",name) #use this way , lot of chances of errors
letter = letter.replace("<|Date|>",date)
print(letter)            