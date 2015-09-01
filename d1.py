#!/usr/bin/python
import sys
import csv



with open("loansDATA.csv") as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
       print(row[1], row[2])

'''
cr = csv.reader(open("loansDATA.csv", "rb"))  # name of object reader is cr
#for row in cr:  # get rows (in the form of a list of columns)
  #  print row
for row in reader:         #prints items in this row with the index as [2],[-2]
 print row[2], row[-2]


import csv
import sys

f = open(sys.argv[1], 'rt')
try:
    reader = csv.reader(f)
    for row in reader:
        print row
finally:
    f.close()



with open("loansData.csv") as f:
    loan = f.next()
    total = 0
    for row in csv.reader(f):
        total += int(row[0])
    print total



def sumRows(loansDATA, header=False):
 d = {}
with open("loansDATA.csv") as csvfile:
        headerline = csvfile.next()
        total = 0
        for row in csv.reader(csvfile):
            total += int(row[1])
print(total)
     #  return()
'''