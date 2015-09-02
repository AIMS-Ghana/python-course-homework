#!/usr/bin/python

import csv

f = open('loansData.csv')
reader = csv.reader(f) 

result = 0.0

for row in reader:
      if 'educational' in row: 
          result = result + float(row[0])

      else:
             pass
print result
