import urllib, json
filename="donuts.json"
thing=json.load(open(filename))
for base_donut in thing:
	base_name=base_donut["name"]
	for batter in base_donut["batters"]["batter"]:
		batter_name=batter["type"] 
		for topping in  base_donut["topping"]:
			topping_name=topping["type"]
			print (base_name+"  "+batter_name+"  "+topping_name) 
	#print base_name




















'''
url = "http://aims-ghana.github.io/python-course/topic/05/donuts.json"
response = urllib.urlopen(url)
data = json.loads(response.read())
print data
json.dumps([1, 'simple', 'list'])
#print data[0]  # will return 'blabla'
#data["masks"]["id"]    # will return 'valore'
#data["om_points"] 
'''
