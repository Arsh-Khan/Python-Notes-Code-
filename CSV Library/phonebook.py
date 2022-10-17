import csv

name = input("Enter your Name : ")
number = int(input("Enter Your Number : "))

with open("phonebook.csv",'a') as file:
    writer = csv.writer(file)
    writer.writerow([name,number])
