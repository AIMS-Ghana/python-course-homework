#!/usr/bin/python3
import sys  

# finding midpoint
def integrate(f,b):
   for n in range (10):
      h=(b[n]-b[n-1])/n
      width=(b[n]-b[n-1])
      midpoint=(b[n]-b[n-1])/2
      y=midpoint+width*h
   return y
