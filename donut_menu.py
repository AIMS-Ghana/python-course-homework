#!/usr/bin/python

import json
#my_data = json.loads(open("donuts.json").read())

#print my_data

my_data = json.load(open("donuts.json"))

for base_donut in my_data:
    base_name = base_donut["name"]
    for batter in base_donut["batters"]["batter"]:
        batter_name = batter ["type"]
        for topping in base_donut["topping"]:
            topping_name = topping ["type"]
            print (base_name + ", "+ batter_name + ", "+ topping_name)
