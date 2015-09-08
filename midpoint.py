#!/usr/bin/python
import math

def integrate (function, rangex):
    n=0.0
    for x in range(len(rangex)-1):

        w=rangex[x+1]-rangex[x]
        h=function(float((rangex[x+1]+rangex[x])/2))
        n += w*h
   
    return n
