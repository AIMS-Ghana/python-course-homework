#!/usr/bin/python

def check (a, b):
    assert a > 0 and b > 0, "negative dimension"

def perimeter(a,b):
	check(a,b)
	perimeter=(a+b)
        return perimeter

import math
def area (a,b):
	check(a,b)
	res=(a*b)
        area= a*b
	return area

import sys

if __name__=="__main__":
	a= float(sys.argv[1])
	b= float(sys.argv[2])
print("area {},perimeter{}".format(area(a,b),perimeter(a,b)))
