#!/usr/bin/python
import math

def integrate(func, rangex):
    total = 0.0
    for x in range(len(rangex)-1):
        a = rangex[x+1]-rangex[x]
        b = func(float((rangex[x+1]+rangex[x])/2))
        total += a*b
	
    return total


	
