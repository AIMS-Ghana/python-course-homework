#!/usr/bin/python

from scipy.integrate import odeint
import numpy as np
import matplotlib.pylab as plt
from scipy.misc import derivative


def plotter(f):
    def g(I,x):
        return f(x)


    plt.figure()
    X = np.arange(0,10,0.01)
    plt.xlabel("x-axis")
    plt.ylabel("y-axis")
    Df = derivative(f,X,dx=1,n=1)
    If = odeint(g, 0, X)
    plt.plot(X,f(X),'y',label='fxn',lw =2)
    plt.plot(X,Df,'b',label='derivative',lw =2)
    plt.plot(X,If,'bo',label='integral',lw =2)
     
    plt.legend()
    plt.show()   
