#!/usr/bin/python
import sys
import csv

total = csv.reader(open("loansData.csv","rb"))
amount = 0.0
for row in total: 
      if 'educational' in row[5]:
                amount += float(row[0])
print amount

