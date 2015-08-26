#!/usr/bin/python
import sys
def area(r,s):
	return r*s
def perimeter(r,s):
	return 2*(r+s)
if __name__=='__main__':
	r=sys.argv[-1]
	s=sys.argv[1]
	r=float(r)
	s=float(s)
	assert s>0 and r>0,"error,there is a negative numbers, please retype"
	a=area(r,s)
	p=perimeter(r,s)
	print "area ",a	
	print "perimeter",p

