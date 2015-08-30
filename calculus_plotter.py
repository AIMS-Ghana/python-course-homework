#!/usr/bin/env python

import sys
import numpy as np
import scipy.integrate as integrate
import numpy as gradient
import matplotlib.pyplot as pyplot



def f_calculus(f, rangex): #dy/dt=func(y,t0)
	def func(f, I):
	    return f(x)
	f=f(x)
	der_f=gradient (fx)
	int_f=integrate.odeint(f, 0.0, rangex)
	f_plot=[f,der_f, int_f]
	return f_plot 
	
	'''
	f_plot:
	{
	f=f(x)
	der_f=gradient f(x)
	int_f=integrate.odeint(f, 0.0, rangex)	
}'''
	
def plot_f(func,x):
	x=(0.0, 5, 0.1)
	y=f_calculus(func, x)
	f=pyplot.plot(x, y[0], color="green")
	der_f=pyplot.plot(x, y[1], color="blue") 
	int_f=pyplot.plot(x, y[2], color="black")
	#plt.legend()	
	plt.show()
	

