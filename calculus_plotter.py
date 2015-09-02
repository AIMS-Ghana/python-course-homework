#!/usr/bin/python

from scipy.misc import derivative
from scipy.integrate import odeint
import matplotlib.pylab as plt
import numpy as np
import fun_plots

def fun_plots(c):
    def m(I,x):
        return c(x)
    plt.figure()
    x = np.arange(0.0, 20.0, 0.01)
    plt.xlabel('x-axis')
    plt.ylabel('y-axis')

    Dfun = derivative(c,x)
    Ifun = odeint(m, 0, x)
    plt.plot(x,c(x), 'g', label= 'f(x)' )
    plt.plot(x,Dfun, 'r', label='Derivative')
    plt.plot(x,Ifun, 'b', label='Integral')

    plt.legend()
    plt.show()
