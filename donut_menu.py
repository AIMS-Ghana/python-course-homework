#!/usr/bin/env python
import json
'''
To load data from the donuts.json and combination of donuts, batters, and (single) toppings

'''

#open donuts.json

with  open("donuts.json") as donutsData:
	donutsData = json.load(donutsData)
#print donutsData

#reading file content

print donutsData[0]



