#!/usr/bin/python

from scipy.integrate import odeint
from scipy.misc import derivative
import numpy as np
from pylab import *


def rhodalin(f):
	figure()
	x = arange(0,10,0.01)

	def l(I,x):
		return f(x)
	If = odeint(l,0,x)

	d = derivative(f,x,dx=1,n=1)
	plot(x,f(x), linestyle= '-', color='y', label= 'function')
	plot(x,d, linestyle= '--', color= 'r', label= 'd/dy(x)')
	plot(x,If, color= 'b', label= 'Integral')
	legend()

	show()



