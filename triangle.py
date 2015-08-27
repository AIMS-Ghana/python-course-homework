
#!/usr/bin/env python

def check(a,b,c):
	s=a+b
	d=a-b
	assert (a>0) & (b>0) & (c>0), "entered negative numbers"
	assert	(s>c)& (d<c),"violated triangle inequality"
# calculate the perimeter

def perimeter(a,b,c):
	check(a,b,c)
	return a+b+c
# calculate the area
def area(a,b,c):
    	check(a,b,c)
	s=(a+b+c)/2
	return (s*(s-a)*(s-b)*(s-c))**0.5
import sys
if __name__ == "__main__":
	a=float(sys.argv[1])
	b=float(sys.argv[2])
	c=float(sys.argv[3])

 	print "area{},perimeter{}".format(area(a,b,c),perimeter(a,b,c))
 
