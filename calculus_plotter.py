#!/usr/bin/python


import midpoint
import numpy as np
from sympy import *
import matplotlib.pyplot as pyplot
from numpy import gradient
import scipy.integrate as integrate



#test functions
def sine_and_cos(t):
    return np.sin(t) + np.cos(t)


def easy(x):
    return x


'''
1. ploting just the function
2. ploting the derivative of the function
3. ploting the integral of the function
'''


def functions_plot(f,nbins):
	def Int(I,x):
		return f(x)
	fx = f(nbins)
	diff_f = gradient(fx)#finds the derivative
	integrate_f = integrate.odeint(Int,0.0,nbins)
	values = [fx,diff_f,integrate_f]
	return values





def _plot(func):
	x = np.arange(-6, 15, 0.05);
	y = functions_plot(func,x)
    	fx, = pyplot.plot(x, y[0], '-')
 	diff_f  = pyplot.plot(x, y[1], '-')
	integral_f = pyplot.plot(x, y[2], '-')
	pyplot.legend([fx,diff_f],['function','derivative'])
    	pyplot.show()
	
	

if __name__ == "__main__":
	_plot(sine_and_cos)
	

