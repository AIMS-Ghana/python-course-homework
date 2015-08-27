#!/usr/bin/python3
def integrate(intf,v):
	h=1/10.0
	z=0
	for i in v:
		j=i/10.0
		z=z+intf((j+j+0.1)/2.0)
	return h*z

	
	
