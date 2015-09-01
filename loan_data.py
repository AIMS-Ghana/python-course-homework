#!/usr/bin/env python
# -*- coding: utf-8 -*-

import csv

cr = csv.reader(open("loansData.csv","rb"))
#sum up the total request amount spent for educations 
# -requested amount in first col of each 

total=0
for row in cr:
	
	if "educational" in row[5]:
		total =total+float(row[1])



print total
