#!/usr/bin/python
<<<<<<< Updated upstream
<<<<<<< Updated upstream
import sys
import pylab
import numpy as np
import fun_plots as fp
from scipy.misc import derivative
from scipy.integrate import odeint

x = np.arange(0,10,0.01) # 100 linearly spaced numbers

def plotter(f):
	pylab.plot(x,f(x), 'b', label = "f(x)")
        pylab.figure()
	def g(I,x):
		return f(x)

	p = odeint(g,0,x)
	df = derivative(f,x,dx=1,n=1)
	pylab.plot(x,f(x), 'g')
	pylab.plot(x,df,'r', label = "f'(x)")
	pylab.plot(x,p,'c', label = "f'(x)")
	pylab.legend()
	pylab.show() # show the plot


plotter(np.cos)

=======

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

plotter(numpy.cos)
>>>>>>> Stashed changes
=======

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

plotter(numpy.cos)
>>>>>>> Stashed changes
