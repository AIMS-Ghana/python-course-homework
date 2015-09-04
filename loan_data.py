#!/usr/bin/python
import csv
mydoc= open('loansData.csv')


total_funds=0

for row in csv.reader(open(mydoc)):

	if row[5]=="educational":
		total_funds= total_funds+float(row[1])
	else:
		pass

print total_funds
	
