#!/usr/bin/python
import sys
from math import*
r=sys.argv[1]
s=sys.argv[2]
t=sys.argv[3]
s=int(s)
r=int(r)
t=int(t)
if s<0 or r<0 or t<0:
	print("##error##\t You have type an negative number, so retry")
	sys.exit()
else:
	p=r+s+t
	d=p/2.0
	a=sqrt(d*abs((d-r)*(d-s)*(d-t)))
print "area ",a
print "perimeter",p
