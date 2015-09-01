#!/usr/bin/python

import csv
f=open('loansData.csv')

csv_f = csv.reader(f)


Total_amount= 0.0

for row in csv_f:
	
	if row[5]== "educational":
		Total_amount= Total_amount + float(row[1])


	else:
		pass
print Total_amount

