#!/usr/bin/python
import numpy as np
import math


def integrate (f, h):
	total = 0.0
	h = 0.1
	for k in range (0, 10):
		total = total + f((0 - 0.5*h + (k * h)))
		return h * total

import sys 
if __name__ == "__main__": 


