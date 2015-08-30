#!/usr/bin/python
import numpy as np
import math


def integrate (f, rangeX):
	ssum = 0
	
	for t in range(len(rangex)-1):
		k = rangex[t + 1] - rangex[t]
		h = f((rangex[t + 1] + rangex[t])/2)
		ssum = ssum + k*h
	return ssum

import sys 
if __name__ == "__main__": 

print 
