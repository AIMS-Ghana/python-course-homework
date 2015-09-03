#!/usr/bin/python
import sys
import csv
myfile="loansData.csv"

tol = 0.0
for row in csv.reader(open(myfile)):
        if row[5] == "educational":
           tol=tol + float(row[1])
print tol
