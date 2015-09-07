#!/usr/bin/python

import json #Necessary module

with open('donuts.json') as data_file:    
    data = json.load(data_file)
for i in range(len (data)):
	for j in range(len(data[i]["batters"]["batter"])):
		for k in range(len(data[i]["topping"])):
			print(data[i]["name"]","data[i]["batters"]["batter"][j]["type"]","data[i]["topping"][k]["type"]"\n")

####################
# An other version #
####################

"""
for base_donut in json.load (open (myfile)):
	base_name = base_donut ["name"]
	for batter in base_donut ["batters"]["batter"]:
		batter_name = batter ["type"]
		for topping in base_donut ["topping"]:
			topping_name = topping ["type"]
			print(base_name + "," + batter_name + "," + topping_name)

"""
