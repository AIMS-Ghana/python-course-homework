#!/usr/bin/python

import csv

loan_data=open('loansData.csv')
data_set=csv.reader(loan_data)

total=0

for row in data_set:
    if "educational" in row:
        total=total + float(row[0])
    else:
         pass

print total
