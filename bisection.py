#!/usr/bin/python

import numpy as np

def root(f, rangex):
	e = 0.0001
	a = rangex[0]
	b = rangex[1]
	while (b - a) > e:
		c = (a + b)/2.0
		if f(c) == 0:
			return c
			break
		else:
			if f(a)*f(c) < 0:
				b = c
			elif f(b)*f(c) < 0:
				a = c
