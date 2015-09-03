#!/usr/bin/python
import math

import time

def integrate (a, b):
    n=0.0
    for i in range(len(b)-1):

        w=b[i+1]-b[i]
        midpoint=float(b[i+1]+b[i]/2)
        h=a(midpoint)
        f=n + w*h
   
    return f
