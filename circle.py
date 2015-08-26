#!/usr/bin/python
def check(radius):
	assert (radius>0),"entered negative dimension"

def area(radius):
	check(radius)
	pi = 3.14159
	res = ( radius ** 2 ) * pi
	return res

def perimeter(radius):
	check(radius)
	pi = 3.14159
	return 2*pi*radius

import sys 
if __name__ =="__main__":
	radius = float(sys.argv[1])
    
	print("area {},\nperimeter {}".format(area(radius), perimeter(radius)))
