#!/usr/bin/python

import json
from collections import defaultdict

df  = json.load(open('donuts.json'))




#print(df)



print(type(df))

for doc in df:
   for key, value in doc.iteritems():
          print key, value








