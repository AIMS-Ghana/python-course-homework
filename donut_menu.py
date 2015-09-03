#!/usr/bin/env python
import sys
import json
#using a json datafile, myfile

for donut_menu in json.load(open("donuts.json")):
    base_name=donut_menu["name"]
    for batter in donut_menu["batters"]["batter"]:
	batter_name=batter["type"]
	 
	for topping in donut_menu["topping"]:
	    topping_name=topping ["type"]
	    
	    print base_name+ "," +batter_name+"," +topping_name

