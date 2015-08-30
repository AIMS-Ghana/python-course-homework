#!/usr/bin/python
import math
import numpy as np
import fun_plots as fp
from pylab import*
from scipy.misc import derivative
from scipy.integrate import odeint

def plotter(fxn):
    def h(I,x):
        return fxn(x)
    plt.figure()
    title("A graph of a function with it's derivative and integral")
    xlabel("X")
    ylabel("Y")
    xticks(arange(0,10,1))
    X = arange(0,10,0.1)
    Dfxn = derivative(fxn,X,dx=1,n=1)
    Ifxn=odeint(h,0,X)
    plot(X,fxn(X), 'r', lw = 2, ms = 3, label = "f(x)")
    plot(X,Dfxn, 'b', lw = 2, ms = 3, label = "f'(x)")
    plot(X,Ifxn, 'y', lw = 2, ms = 3, label = "integration")
    legend(loc=0)
    plt.show()
