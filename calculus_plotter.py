#!/usr/bin/python
import sys
import pylab
import numpy
import fun_plots as fp
from scipy.misc import derivative

x = numpy.arange(0,10,0.01) # 100 linearly spaced numbers
# compose plot

def plotter(f):
	pylab.figure()
	df = derivative(f,x,dx=1,n=1)
	
	pylab.plot(x,f(x), 'b', label = "f(x)")
	pylab.plot(x,df,'r', label = "f'(x)")
	pylab.legend()
	pylab.show() # show the plot


