#!/usr/bin/python
import math
import numpy as np
import fun_plots as fp
from matplotlib.pyplot import *
from scipy.misc import derivative
from scipy.integrate import odeint

def plotter(fxn):
    def t(I,X):
        return fxn(X)
    figure()

    title("A graph of a function with it's derivate and integral")
    xlabel("X")
    ylabel("Y")
    xticks(arange(0,10,1))
    X=arange(0,10,0.1)
    Dfxn = derivate(fxn,X,dx=1,n=1)
    Ifxn=odeint(t,0,X)
    plot(X, fXn(X), 'b', lw = 2, label = "f(x)")
    plot(X, Dfxn(X), 'r', lw = 2, label = "f(x)")
    plot(X, Ifxn(X), 'bo', lw = 2, label = "integration")
    legend(loc=0)
    plt.show()

