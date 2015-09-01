#!/usr/bin/python
import sys
from random import *
 
N=int(sys.argv[2])
Inside_value = 0
Total_value = 0
for i in range (0, N):
    r = random ()
    s = random ()
    if r**2 + s**2 <= 1:
        Inside_value = Inside_value + 1
   
print "circle-area pi = {}".format(float(4*Inside_value)/N)
for i in range (0, N):
    l = random ()
    m = random ()
    k = random () 
    if l**2 + m**2 + k**2 <=1:
        Total_value = Total_value + 1
print "sphere-volume pi = {}".format(float(6*Total_value)/N)

