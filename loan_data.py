#!/usr/bin/python

import csv

loan_data = open('loansData.csv')
data_set = csv.reader(loan_data)

Total_amount = 0.0

for row in data_set:
	if "educational" in row:
		Total_amount = Total_amount + float(row[0])
	else:
		pass

print Total_amount
import


