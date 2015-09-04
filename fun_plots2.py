#!/usr/bin/python

import numpy as np
import calculus_plotter as cp


def sin2(x):
	return np.sin(2*x)

def square(x):
	return (x**2)

def x_exp(x):
	return (x**2)*np.exp(x)

def cos(x):
	return np.cos(x)

def sin(x):
	return np.sin(x)

funclist1 = [sin2, square, x_exp, cos, sin]

if __name__ == "__main__":
	for n in np.arange(0,5):
		cp.plotter(funclist1[n])
