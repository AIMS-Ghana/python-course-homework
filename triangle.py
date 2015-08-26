#!/usr/bin/python
import sys
from math import*
def area(r,s,t):
	d=(r+s+t)/2.0
	return sqrt(d*(d-r)*(d-s)*(d-t))
def perimeter(r,s,t):
	return r+s+t
if __name__=='__main__':
	r=sys.argv[1]
	s=sys.argv[2]
	t=sys.argv[3]
	s=float(s)
	r=float(r)
	t=float(t)
	c=r+s
	b=r-s
	assert (c>t) & (b<t), "triangle inegality false"
	assert (s>0) and (r>0) and (t>0),"entered negative dimension"
	p=perimeter(r,s,t)
	a=area(r,s,t)
	print "area ",a
	print "perimeter",p

