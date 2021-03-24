# Write a python program to read specific columns of a given csv file and print the content of the column

import csv
header = ["place", "name", "age"]
with open("program4.csv", "w") as file:
    write = csv.DictWriter(file, fieldnames=header)
    write.writeheader()
    write.writerow({"place": "Nedumkandam", "name": "Aparna", "age": 23})
    write.writerow({"place": "Kanjirapally", "name": "Alphons", "age": 24})
    write.writerow({"place": "Kottayam", "name": "Unni", "age": 25})
    write.writerow({"place": "Kochi", "name": "Appu", "age": 14})
with open("program4.csv", "r") as file:
    read = csv.DictReader(file);
    n = input("Enter the  column name you want(place,name,age):")
    for i in read:
        print(i[n])