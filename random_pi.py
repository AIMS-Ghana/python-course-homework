#!/usr/bin/python

import math
import random
import sys

def pointincircle(x, y, cx, cy, radius):
    return math.sqrt((x- cx)**2+ (y-cy)**2) <=radius

    x = float(sys.argv[1])
    y = float(sys.argv[2])

def approximatecirclearea(radius, numberofpoints):
     squareside = radius*2
     cx = radius
     cy = radius

     q = 0
     for i in range(numberofpoints):
	x = random.random()*squareside
	y = random.random()*squareside
     
        if (pointincircle(x, y, cx, cy, radius)):
	    q = q + 1
 
     return q / numberofpoints * squareside**2
print ("Circle-area:", "{}".format(approximatecirclearea))
