#!/usr/bin/python
import sys
import math
def area(r):
	return math.pi*(r**2)
def perimeter(r):
		return 2*math.pi*r
if __name__=='__main__':
	r=float(sys.argv[1])
	if(r<0):
		print("Error, you have been type an negative number. Retry")
		sys.exit()
	else:
		a=area(r)
		p=perimeter(r)
		print"area ", a
		print "perimeter",p	
		a=area(r)
		p=perimeter(r)

