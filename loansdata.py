#!/usr/bin/python
import csv

myfile = "loansData.csv"

total = 0

for row in csv.reader(open(myfile)):
    if row[5] == "educational":
        total = total + float(row[1])
print(total)
