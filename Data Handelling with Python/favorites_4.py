import csv

title = input("Title : ").strip().upper()
count =0
with open("Favorite.csv",'r') as file:
    reader = csv.DictReader(file)

    for row in reader:
        if row["Name of your Favorite tv show"].strip().upper()==title:
            count +=1

print(count)