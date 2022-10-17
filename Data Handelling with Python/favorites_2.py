import csv

count = 0
with open("Favorite.csv",'r') as file:
    reader = csv.DictReader(file)

    for row in reader:
        title = row["Name of your Favorite tv show"].strip().upper()
        # if title == "THE OFFICE" or title == "OFFICE":
        if "OFFICE" in title:  #thevoffice also gets added
            count+=1
        
        

print(f"The number of people liking THE OFFICE is : {count}")            