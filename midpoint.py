#!/usr/bin/env python
import math
import sys
import numpy as np


def integrate(f, rangex):
	toto = 0.0
	for x in np.arange(len(rangex)-1):
		w = rangex[x+1]-rangex[x]
		h= f(float((rangex[x+1]+rangex[x])/2.0))
		toto = toto + h*w
	
	return toto
