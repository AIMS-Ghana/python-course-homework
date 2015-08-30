#!/usr/bin/python

import math
from pylab import *
from scipy.misc import derivative
import fun_plots as fp



from scipy.integrate import quad
import numpy as np

def fxn():
    X= 1 - np.exp(-x)
    Dfxn = derivative(fxn,X,dx=1,n=1)
    return X



def plotter(fxn):
    figure()
    title("A graph of a function with it's derivative and integral")
    xlabel("X")
    ylabel("Y")




    xticks(arange(0,10,1))   
    #Ifxn= integrate.quad(fxn,X)
    plot(X,fxn(X), 'r', lw = 2, ms = 3, label = "f(x)")
    plot(X,Dfxn, 'b', lw = 2, ms = 3, label = "f'(x)")
    plot(X,Ifxn, 'g', lw = 2, ms = 3, label = "f'(x)")
    legend()
    

