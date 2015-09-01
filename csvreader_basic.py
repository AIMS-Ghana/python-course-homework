#!/usr/bin/python3

import pandas as pd

df = pd.read_csv('loansData.csv')

sum = 0

for i in range(len(df)):
  if df.iloc[i,5] == 'educational':
     sum = sum + df.iloc[i,2]
        

print(sum)


        
