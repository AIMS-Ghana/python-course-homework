#!/usr/bin/env python3

import csv

myfile = "loansData.csv"

## sum up the total requested amount for education
##  - requested amount in first col of each row
##  - rows for education, have "educational" in them

#total = 0
#for row in csv.reader(open(myfile)):
#    if row[5] == "educational": # find education some way
#        total = total + float(row[1])
#print(total)

import pandas

data = pandas.read_csv(myfile)
print(sum(
  data[data['Loan.Purpose'] == "educational"]['Amount.Requested']
))








