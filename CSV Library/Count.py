import csv   #csv files-files database

destination = {
    "Dubai":0,
    "Singapore":0,
    "Malaysia":0,
    "London":0
}

with open("D:\HDD Data 22-03-22\C data\Desktop\python\CSV Library\survey.csv",'r') as file:
    # reader = csv.reader(file)
    reader = csv.DictReader(file)
    next(reader)   # Skips a row 
    for row in reader:
        # des = row[1]
        des = row["Which is your favorite vacation destination"]
        destination[des] +=1

for des in destination:
    count = destination[des]
    print(f"{des} : {count}")
