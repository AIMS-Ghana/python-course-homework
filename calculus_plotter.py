#!/usr/bin/python

import matplotlib.pyplot as plt
import numpy as np
from numpy import gradient
import scipy.integrate as integrate


def sine_and_cos(t):
    return np.sin(t) + np.cos(t)


def dervs(f,rangex):
	def Func(f,x):
		return f(x)
	f_x = f(rangex)
	d_f = gradient(f_x)
        I_f = integrate.odeint(Func,0.0,rangex)
        results = [f_x,d_f,I_f]
	return results

def plotter(func):
        x = np.linspace(0,20,100,True)
        y = dervs(func,x)
	plt.plot(x, y[0])#the function
	plt.plot(x, y[1])#the derivative
	plt.plot(x,y[2])#the integral
	plt.show()

#in makefunplotter, import funplots and calculus inorder to plot graphs

if __name__ == "__main__":
	plotter(sine_and_cos)



