#!/usr/bin/python
import sys
import pylab
import numpy
import fun_plots as fn
from scipy.misc import derivative
from scipy.integrate import odeint
x = numpy.arange(0,10,0.01) # 100 linearly spaced numbers
# compose plot

def plotter(f):
	pylab.figure()
	df = derivative(f,x,dx=1,n=1)
	
	def g(I,x):
		return f(x)
	If = odeint(g,0,x)
	
	pylab.plot(x,f(x), 'b', label = "f(x)")
	pylab.plot(x,df,'r', label = "f'(x)")
	pylab.plot(x,If, 'g', label = "intf(x)")
	
	pylab.legend()
	pylab.show() # show the plot

#plotter(numpy.cos)
