#!/usr/bin/env python
import math
import numpy as np
import matplotlib.pyplot as plt
from scipy.misc import derivative as deriv
from scipy.integrate import odeint

def func(g,x):
	return g(x)

def plotter(f):
	def h(I,x):
		return f(x)
	init = 0
	x = np.arange(-10.0, 20.0, 0.01) # range of x values on graph
	y,dydx,i = func(f,x),deriv(f,x),odeint(h,init,x)  # define the y values on graph
	plt.plot(x,y,'r', label='f(x)') # plot x against y
	plt.plot(x,dydx,'g', label= 'dydx')
	plt.plot(x,i,'b', label = 'integral')
	plt.xlabel('x-axis') # label x-axis
	plt.ylabel('y-axis') # label y-axis
	plt.ylim(-5,5)
	plt.legend()
	plt.show() # show graph


if __name__ == "__main__":
	plotter(np.sin)
