#!/usr/bin/env python

import csv #to read loansData.csv file
import sys
csvfile = open('loansData.csv', 'r')
reader = csv.reader(csvfile)
headers=reader.next()
sum_ed=0
for row in reader:
	if "educational" in row: #summing funds requested for education
		sum_ed=sum_ed + float(row[0])        
	else:
		pass
print sum_ed
