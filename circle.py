#!/usr/bin/env python
import math



def check(a):
	assert a>0, "enter positive numbers"

def area(a):
	check(a)
	result= math.pi*a*a
	return result
def perimeter(a):
	check(a)
	value=2*math.pi*a
	return value
import sys
if __name__=="__main__":
	a=float (sys.argv[1])	
	print("area{}, perimeter{}".format(area(a), perimeter(a)))
