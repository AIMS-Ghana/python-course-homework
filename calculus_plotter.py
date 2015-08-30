#!/usr/bin/python
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


def main(func):
	
    x = np.arange(0.0, 5.0, 0.01)
    y = figures(func,x)
    fx= pyplot.plot(x,y[0],'-')
    df= pyplot.plot(x,y[1],'-')
    IF= pyplot.plot(x,y[2],'-')
    #pyplot.plot(x,y[2],'-')
   
    pyplot.show()



if __name__ == "__main__":
	main(sine_and_cos)

