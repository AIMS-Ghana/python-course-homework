#!/usr/bin/python
import math

def integrate(func, rangex):
    ssum = 0.0
    for x in range(len(rangex)-1):
        a = rangex[x+1]-rangex[x]
        b = func(float((rangex[x+1]+rangex[x])/2))
        ssum += a*b
	
    return ssum


	
