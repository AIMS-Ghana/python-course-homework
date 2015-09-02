#!/usr/bin/python

import csv

myfile = "loansData.csv"

# sum the total requested amount for the educational 
# rows for education, have "educational" in row

total = 0
for row in csv.reader(open(myfile)):
    if row[5] == "educational":
        total = total + float(row[1])
print(total)









    
