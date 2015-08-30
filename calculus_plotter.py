#!/usr/bin/python

from scipy.misc import derivative
import numpy as np 
from pylab import *
from scipy.integrate import odeint

def plotter(f):
	figure(),grid(True)					# to set up figure
	X = np.arange(0,10,0.01)				# to define the domain of the graph
	plot(X,f(X), 'r', label = "f(x)")			# to plot the graph
	

	Df = derivative(f,X,dx=1,n=1)				# to differentiate f
	plot(X,Df, 'b', label = "f'(x)")			# to plot the derivative of f

	def g(I,X):
		return f(X)					# to integrate f					
	If = odeint(g,0,X)

	plot(X, If, 'c', label = r'$\int(f(x)dx)$')		# to plot the integral of f

	legend()						# to show the legend
	show()							# to show the graph on the figure

if __name__ == "__main__":
		plotter(np.sin)
