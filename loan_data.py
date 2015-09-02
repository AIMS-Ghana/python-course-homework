#!/usr/bin/python

import csv

bni ="loansData.csv"

tot=0

for row in csv.reader(open(bni)):

      if row[5] =="educational": 
          result = tot + float(row[1])


print result
