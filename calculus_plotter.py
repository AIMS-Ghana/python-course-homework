#!/usr/bin/python

from scipy import odient
import numpy as np
import matplotlib.ply as pyplot
from scipy.misc import derivative


def plotter(f):
    def g(I,x):
        return f(x)


    plt.figure()
    x = np.arange(0,10,0.01)
    plt.xlabel("x-axis")
    plt.ylabel("y-axis")
    Df = derivative(f,x,dx=1,n=1)
    If =odeint(g, 0, x)
    plt.plot(X,f(x),'y',label='fxn',lw =2)
    plt.plot(X,Df,'b',label='derivative',lw =2)
    plt.plot(X,If,'bo',label='integral',lw =2)
     
    plt.legend()
    plt.show()   
