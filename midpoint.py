#!/usr/bin/python
from math import *
import sys
def integrate(f,rangex):
	h=float(rangex[1]-rangex[0])
	assert h>0

	sum=0.0
	midpoint=rangex[0]+h/2
	while (midpoint<rangex[1]):
		sum+= h*f(midpoint)
		midpoint+=h
	return sum
	
 	
		
	
