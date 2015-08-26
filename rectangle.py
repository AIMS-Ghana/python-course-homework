#!/usr/bin/env python3






def check(a,b):
	assert (a>0) & (b>0)  ,"inserted negative integers"
	

def area(a:float,b:float):
	check(a,b)
	res=a*b
	return res


def perimeter(a,b):
	check(a,b)
	rest=(a+b)*2
	return rest

import sys

if __name__=="__main__":
	a=float(sys.argv[1])
	b=float(sys.argv[2])
	print ("area {},perimeter {}".format(area(a,b), perimeter(a,b)))

	
