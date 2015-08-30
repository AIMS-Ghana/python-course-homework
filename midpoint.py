#!/usr/bin/python
import numpy as np
import math


def integrate (f, rangex):
	total = 0.0
	for x in range(len(rangex)-1):
	    s=(rangex[x+1]-range[x])
            h=f(float[x+1]+range[x])/2	
            total + =s*h 
		return  total

import sys 
if __name__ == "__main__": 


