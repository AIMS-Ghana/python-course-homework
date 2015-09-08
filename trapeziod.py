#!/usr/bin/python

def integrate(intf, rangex):
     area =0.0
     for x0 in range(len(rangex)-1):
		a = intf(rangex[x0])
		b = intf(rangex[x0+1])
		c = rangex[x0+1]-rangex[x0]
		d = (a+b)*0.5
		area = d*c
		
     return area
	
	
