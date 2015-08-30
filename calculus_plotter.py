#!/usr/bin/python


import numpy as np
import matplotlib.pyplot as plt
from scipy.misc import derivative as dev
from scipy.integrate import odeint as odt


def sine(t):
    return np.sin(t) 

def func(g,xr):
        fx = g(xr)
	return fx


def plotter(f):
	def h(I, x):
          return f(x)
	t = np.arange(0.0,10.0, 0.01)
       	y = func(f,t)
	yd = dev(f,t)
	yi = odt(h,0,t)
	line1 = plt.plot(t,y,'r', label="f(x)",lw=2)
	line2 = plt.plot(t,yd,'g',label="derivative",lw=2)
	line3 = plt.plot(t,yi,'b',label="integral",lw=3)
	plt.ylim(-2,2)
	plt.legend()
	plt.show()


if __name__ == '__main__':
	plotter(sine)
	
	
	
