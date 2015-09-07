#!/usr/bin/python

import csv #Necessary module

cr = csv.reader(open("loansData.csv"))
cr.next()
ammount_requested = 0

for x in cr:
	if x[5] == "educational":
		ammount_requested += float(x[1])
print "The ammount requested for education is {}".format(ammount_requested)

####################
# An other version #
####################

"""
import pandas

data = pandas.read_csv ('loansData.csv')

print(sum(data[data['Loan.Prupose'] == "educational"] ["Amount.Requested"]))

"""
