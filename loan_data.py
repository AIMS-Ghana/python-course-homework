#!/usr/bin/env python

'''
To load data from the loansData.csv and calculate the total amount of requested funds for education
Note: Assume first column in loansData.csv to be ID :)
'''

import csv

sum_ =0.0
with open("loansData.csv",'r') as csvfile:#open loansData.csv
	loansData = csv.reader(csvfile)
	
	for line in loansData:
	    if 'educational' in line[5]:
		  sum_ += float(line[1]) #sum amount requested for educational

print '\nTotal Amount requested for education is: ', sum_




