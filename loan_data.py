#!/usr/bin/env python

'''
To load data from the loansData.csv and calculate the total amount of requested funds for education

'''
#open loansData.csv
loansData = open("loansData.csv", "r")

#reading file content
sum_ =0.0
for line in loansData:
    columns = line.split(',')
    if len(columns) >= 1:
        if 'educational' in columns[5]:
                 sum_ += float(columns[0].replace('"', '').strip()) #sum amount requested for educational
print 'Total Amount requested for education is: ', sum_
loansData.close() #close loansData file



