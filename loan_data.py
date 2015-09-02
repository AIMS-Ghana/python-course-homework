#!/usr/bin/python
import csv

my_data = csv.reader (open ("loansData.csv"))
total = 0
for row in my_data:
   if row[5] == "educational":
      total +=float(row[1])
   print (total)

"""myfile = csv.reader(open ("loansData.csv"))
c.next()
total = 0
for row in c:
   total += float(row[1])
print(total)"""
