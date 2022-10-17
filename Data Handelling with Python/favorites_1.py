import csv
# counting occurances of show
titles = {}
with open("Favorite.csv",'r') as file:
    reader = csv.DictReader(file)

    for row in reader:
        
        title = row["Name of your Favorite tv show"].strip().upper()
        
        if not title in titles:
            titles[title] = 0
        
        titles[title] += 1    
        
        # if title in titles:
        #     titles[title]+=1
        # else:
        #     titles[title] = 1    


for title in sorted(titles ,key= lambda title:titles[title] ,reverse=True):  #sorted can pass function name and not function definition
    print(title,titles[title])


# def get_value(title):
#     return titles[title]

# for title in sorted(titles ,key=get_value ,reverse=True):  #sorted can pass function name and not function definition
#     print(title,titles[title])


# ------------

# for title in sorted(titles , reverse=True):  #sorted sorts acc to key of dictionary
#     print(title,titles[title])