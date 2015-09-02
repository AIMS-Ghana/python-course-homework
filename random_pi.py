#!/usr/bin/python
import sys
from random import *
 
n = int(sys.argv[2])
total_inside = 0.0
TOTAL_INSIDE = 0.0
for k in range (0, n):
    x = random ()
    y = random ()
    if x**2 + y**2 <= 1:
        total_inside = total_inside + 1
   
print "circle-area pi = {}".format(float(4*total_inside)/n)
for k in range (0, n):
    X = random ()
    Y = random ()
    Z = random () 
    if X**2 + Y**2 + Z**2 <=1:
        TOTAL_INSIDE = TOTAL_INSIDE + 1
print "sphere-volume pi = {}".format(float(6*TOTAL_INSIDE)/n) 

