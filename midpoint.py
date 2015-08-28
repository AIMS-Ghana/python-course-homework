#!/usr/bin/python
import numpy as np
import math

def calc_h (a, b, n):
	return (b-a) /float (n)

def mid_pt (f, h):
	total = 0.0
	h = calc_h (a, b, n)
	for k in range (0, 10):
		total = total + f((0 - 0.5*h + (k * h)))
		return h * total
def f(x):
	return np.exp(x)

import sys 
if __name__ == "__main__": 

	print mid_pt (intf,0, 10, 100)
