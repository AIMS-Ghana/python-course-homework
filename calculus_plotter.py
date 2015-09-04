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
	func_names = [r'$f(x) = x$',r'$f(x) = 1 - e^{-x}$', r'$f(x) = e^{5x}$',r'$f(t) = \sin(t) + \cos(t)$',r'$f(t) = \sin^{2}(t)$']
	for i in range (0,5):
		funclist=(i+1)
	#fig = plt.figure() 
	#fig.suptitle("Graph of {0} together with its derivative and integral",format.(func_names))
	fig = plt.figure()
	#plt.plot(data)
	fig.suptitle('graph of {}'.format.func_names(i),'with its derivative and integral')
	x = np.arange(-30.0, 30.0, 0.0001) # range of x values on graph
	y,dydx,i = func(f,x),deriv(f,x),odeint(h,init,x)  # define the y values on graph
	plt.plot(x,y,'r', lw = 2, label='f(x)') # plot x against y
	plt.plot(x,dydx,'g', lw = 2, label= 'dydx')
	plt.plot(x,i,'b', lw = 2, label = r'$\int{f(x)}dx$')
	plt.xlabel('x-axis') # label x-axis
	plt.ylabel('y-axis') # label y-axis
	plt.ylim(-5,5)
	plt.legend()
	mng = plt.get_current_fig_manager()
	mng.frame.Maximize(True)
	plt.show() # show graph


if __name__ == "__main__":
	plotter(np.sin)
