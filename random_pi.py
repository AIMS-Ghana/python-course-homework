#!/usr/bin/python
import sys


from random import *
 
A = int(sys.argv[2]) 
total_inside = 0
TOTAL_INSIDE = 0


for r in range (0, A):
    C = random ()
    B = random ()
    if C**2 + B**2 <= 1:
        total_inside = total_inside + 1
    
print "circle-area pi = {}".format(float(4*total_inside)/A) 
for r in range (0, A):
    C = random ()
    B = random ()
    N = random ()  
    if C**2 + B**2 + N**2 <=1:
        TOTAL_INSIDE = TOTAL_INSIDE + 1

print "sphere-volume pi = {}".format(float(6*TOTAL_INSIDE)/A)

