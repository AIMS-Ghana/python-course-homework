#!/usr/bin/python
from scipy.integrate import odeint

# I(x) = integral(f)
# dIdx = f(x) = ...some user defined f
# odeint wants f(I,x) to solve for I


import sys
import midpoint
import numpy as np
import scipy.integrate as integrate
from numpy import gradient
import matplotlib.pyplot as pyplot
def sine_and_cos(t):
    return np.sin(t) + np.cos(t)


		
def figures(f,rangex):
	def num(f,i):
		return f(i) 
	fx = f(rangex)
	df = gradient(fx)
    	IF = integrate.odeint(num, 0.0, rangex)	
       	fig=[fx,df,IF]
	return fig

def plot_all(f, rangex, ifxmin = 0):
    lines = calc_all(f, rangex, ifxmin)
    fx, = pyplot.plot(rangex, lines['f'], '-')
    df, = pyplot.plot(rangex, lines['df'], ":")
    If, = pyplot.plot(rangex, lines['If'], "--")
    pyplot.legend([fx, df, If],['function','derivative','integral'])
    pyplot.show()
'''
def main(func):
	
    x = np.arange(0.0, 5.0, 0.01)
    y = figures(func,x)
    fx= pyplot.plot(x,y[0],'-')
    df= pyplot.plot(x,y[1],'-')
    IF= pyplot.plot(x,y[2],'-')
    #pyplot.legend([fx,diff_f, integral_f],['function','derivative','Integral'])
   
    pyplot.show()
'''


if __name__ == "__main__":
	main(sine_and_cos)
'''

