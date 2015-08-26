#!/usr/bin/python

import math
def check (d):
    assert d > 0, "negative dimension"

def perimeter(d):
	pi=3.142	
	check(d)
	perimeter= pi * d
        return perimeter


def area (d):
	pi=3.142
	check(d)
        area= (pi*d)/4
	return area

import sys

if __name__=="__main__":
	d= float(sys.argv[1])
print("area {},perimeter{}".format(area(d),perimeter(d)))
