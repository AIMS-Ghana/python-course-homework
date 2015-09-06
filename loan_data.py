#!/usr/bin/python3


# Obtain data file
import csv
file = "loansData.csv"


# Pandas implementation
import pandas
loan_data = pandas.read_csv(file)
print(sum(loan_data[loan_data['Loan.Purpose'] == "educational"]['Amount.Requested']))
