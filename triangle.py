#!/usr/bin/env python3

def check(a,b,c):
	assert (a>0) & (b>0) & (c>0) ,"inserted negative integers"
	s=a+b
	d=a-b
	assert (s>c) & (d<c) , "violated triangle inequality"



def area(a,b,c):
	check(a,b,c)
	s = (a + b + c) / 2

	# calculate the area
	res= (s*(s-a)*(s-b)*(s-c)) ** 0.5
	return res


def perimeter(a,b,c):
	check(a,b,c)
	ress=a+b+c
	return ress















import sys

if __name__=="__main__":
	a=float(sys.argv[1])
	b=float(sys.argv[2])
	c=float(sys.argv[3])
	check(a, b, c)
	print ("area {},perimeter {}".format(area(a,b,c), perimeter(a,b,c)))


	
