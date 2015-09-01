#!/usr/bin/env python
import json
'''
To load data from the donuts.json and combination of donuts, batters, and (single) toppings

'''

#open donuts.json

with  open("donuts.json") as donutsData:
	donutsData = json.load(donutsData)

#reading file content
print 'Available batters and toppings combinations:\n'
for i in range(len(donutsData)):
  # Looping through batter and toppings for each donut
 
   for n in range(len(donutsData[i]['batters']['batter'])):
        print '\n For',donutsData[i]['name'],donutsData[i]['batters']['batter'][n]['type'],'Donut We have:'
        print '________________________________________'
        for k in range(len(donutsData[i]['topping'])):

                print k+1,'|',donutsData[i]['name'], donutsData[i]['batters']['batter'][n]['type'],donutsData[i]['topping'][k]['type']



