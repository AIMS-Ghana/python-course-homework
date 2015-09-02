#!/usr/bin/env python
import sys
import json

#loading donuts json file

donut_file='donuts.json'

for donut_menu in json.load(open(donut_file)):
    base_name=donut_menu["name"]
    for batter in donut_menu["batters"]["batter"]:
	batter_name=batter["type"]
	 
	for topping in donut_menu["topping"]:
	    topping_name=topping ["type"]
	    
	    print base_name+ "," +batter_name+"," +topping_name
	   
	

