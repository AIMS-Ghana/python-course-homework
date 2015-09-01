#!/usr/bin/python
import csv

total = csv.reader(open("loansData.csv","rb"))
amount = 0.0
for row in total: 
      if 'educational' in row[5]:#find education in the row
                amount += float(row[1])
print amount

