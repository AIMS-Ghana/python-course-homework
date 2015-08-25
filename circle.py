#!/usr/bin/python
import sys
#print(sys.argv[1])
pi=3.14
r=int(sys.argv[1])
if(r<0):
	print("Error, you have been type an negative number. Retry")
	sys.exit()
else:
	a=pi*(r**2)
	p=2*pi*r
	print"area ", a
	print "perimeter",p
