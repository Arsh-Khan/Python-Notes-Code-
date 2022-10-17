import csv
import re  #used for cleaning or validating data --- re stands for regular expression
count = 0
with open("Favorite.csv",'r') as file:
    reader = csv.DictReader(file)

    for row in reader:
        title = row["Name of your Favorite tv show"].strip().upper()
        # actual the office or office available are 3 and one thevoffice is available
        
        if re.search("^(OFFICE|THE OFFICE)$",title): 
            count+=1
        
        # if re.search("^(OFFICE|THE.OFFICE)$",title):  #. considers some char in between them the office 
            # count+=1   #gives output of 4
        
        

print(f"The number of people liking THE OFFICE is : {count}")  