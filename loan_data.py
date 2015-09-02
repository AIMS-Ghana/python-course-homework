#!/usr/bin/python

import csv

f = open('loansData.csv')
reader = csv.reader(f) 

sum = 0.0

for row in reader:
      if 'educational' in row: 
          sum = sum + float(row[1])

      else:
             pass
print sum
