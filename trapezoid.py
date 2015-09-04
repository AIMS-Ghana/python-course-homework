#!/usr/bin/python
import math

def integrate(funcntion, rangex):
    
    total = 0.0
    for x in rangex:
        s = (rangex[x+1]-rangex[x])/2
        fa=float(rangex[0])
        fb=float(rangex[-1])
        h= funcntion(float(fa + fb))
        total = total + h*s
        return total

       


