#!/usr/bin/env python
#to read loansData.csv file
import csv 
import sys
#summing funds requested for education

csvfile = open('loansData.csv', 'r')
reader = csv.reader(csvfile)
headers=reader.next()
sum_ed=0
for row in reader:
	if row[5]=="educational":
		sum_ed=sum_ed + float(row[1])        
	else:
		pass
print sum_ed
