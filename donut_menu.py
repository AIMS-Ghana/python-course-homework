#!/usr/bin/python
import json

for base in  json.load(open("donuts.json")):
	base_n=base["name"]
	for batter in base["batters"]["batter"]:
		batter_n=batter["type"]
		for topping in base["topping"]:
			topping_n=topping ["type"]
			print(base_n+", "+batter_n+", "+topping_n)



	
s



