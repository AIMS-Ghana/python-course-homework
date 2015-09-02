#!/usr/bin/env python
import sys
from random import *  
from math import sqrt  
inside = 0
  
 
for pic in range  (int(sys.argv[2])):
	pic=pic+1
	x=random()  
	y=random()  
  	if (x*x+y*y)<=1:  
  		inside =inside +1  
	pi=4*inside/float(sys.argv[2]) 
print "circle-area  pi:", pi  

inside = 0
for pic in range  (int(sys.argv[2])):
	pic=pic+1
	x=random()  
	y=random() 
	z=random() 
  	if (x*x+y*y+z*z)<=1:  
  		inside =inside +1  
	pi=6*inside/float(sys.argv[2])
print "sphere-volume pi:", pi 
