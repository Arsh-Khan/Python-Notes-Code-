import csv

# titles = []
titles = set()
with open("Favorite.csv",'r') as file:
    reader = csv.DictReader(file)

    for row in reader:
        
        title = row["Name of your Favorite tv show"].strip().upper()
        titles.add(title)
        # if not title in titles:
        #     titles.append(title)


for title in sorted(titles):
    print(title)

# import csv

# with open("Favorite.csv",'r') as file:
#     reader = csv.reader(file)
    #   next(reader)
#     for read in reader:
#         print(read[1])