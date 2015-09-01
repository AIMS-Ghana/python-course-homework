#!/usr/bin/python
import math
import numpy as np
import fun_plots as fp

from matplotlib.pyplot import *

from scipy.misc import derivative
from scipy.integrate import odeint

def plotter(fxn):
    def t(I,x):
        return fxn(x)

    figure()
    title("A graph of a function with it's derivate and integral")
    xlabel("X")
    ylabel("Y")
    #xtick(arange(0,10,1))
    X=np.arange(0,10,0.1)
    Dfxn = derivative(fxn,X,dx=1,n=1)
    Ifxn = odeint(t,0,X)
    plot(X, fxn(X), 'b', lw = 4, ms = 2, label = "f(x)")
    plot(X, Dfxn, 'r', lw = 4, ms = 2, label = "f'(x)")
    plot(X, Ifxn, 'b', lw = 4, ms = 2, label = "integration")
    legend(loc=0)
    show()

