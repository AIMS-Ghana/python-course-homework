#!/usr/bin/python

import sys
from random import *
 
num = int(sys.argv[2])
total = 0
TOTAL = 0
for i in range (0, num):
	    x = random ()
	    y = random ()
	    if x**2 + y**2 <= 1:
	       total = total + 1
	   
print "circle-area pi : {}".format(float(4*total)/num)

for i in range (0, num):
	    X = random ()
	    Y = random ()
	    Z = random () 
	    if X**2 + Y**2 + Z**2 <=1:
	       TOTAL = TOTAL + 1
print "sphere-volume pi : {}".format(float(6*TOTAL)/num)

