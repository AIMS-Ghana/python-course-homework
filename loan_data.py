#!/usr/bin/python

import csv

data = open('loansData.csv')
reader= csv.reader(data)

Total = 0.0

for row in reader:
	if "educational" in row:
		Total = Total + float(row[1])
	else:
		pass

print Total



