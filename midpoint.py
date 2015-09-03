#!/usr/bin/python
import math
import time
import midpoint
import trapezoid


def integrate (f, rangex):
    for i in range(len(rangex)-1):

        w = (range[i+1]-range[i])

        ss=ss+w*h

        h=f(rangex[i+1]+rangex[i])/2
        return ss
    
if __name__ == "__main__":

   print(integrate(lambda x:x, thing))

def integrate (a, b):
    n=0.0
    for i in range(len(b)-1):

        w=b[i+1]-b[i]
        midpoint=float(b[i+1]+b[i]/2)
        h=a(midpoint)
        f=n + w*h
   
    return f
