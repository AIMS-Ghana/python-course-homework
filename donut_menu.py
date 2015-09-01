#!/usr/bin/python

import json
#with open('donutmenu.json') as data_file:
myfile="donutmenu.json"
for menu_donut in json.load(open(myfile)):
    base_name=menu_donut["name"]
    for batter in menu_donut["batters"]["batter"]:
	batter_name=batter["type"]
	for topping in menu_donut["topping"]:
		topping_name=topping["type"]

		print (base_name+", "+batter_name+","+topping_name)
