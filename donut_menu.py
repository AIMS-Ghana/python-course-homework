#!/usr/bin/python

import json

myfile="donuts.json"

for base_donut in json.load(open(myfile)):

    base_name=base_donut["name"]

    for batter in base_donut["batters"]["batter"]:
        batter_name=batter["type"]
	
        for topping in base_donut["topping"]:
            topping_name=topping["type"]
  
            print (base_name+","+batter_name+","+topping_name)

