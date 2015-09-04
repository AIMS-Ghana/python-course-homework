#!/usr/bin/python
import csv
csvfile = csv.reader(open("loansData.csv"))
csvfile.next()
ammount = 0
for x in csvfile:
#print ammount
	if x[5] == "educational":
		ammount += float(x[0])
print "...the sum of educational fund is ", ammount

