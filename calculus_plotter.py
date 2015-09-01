#!/usr/bin/python

import matplotlib.pylab as plt
import numpy as np
from scipy.misc import derivative
from scipy.integrate import odeint

def plotter(fxn):
     def h(I,x):
        return fxn(x)

     plt.figure()
     X = np.arange(0,10,0.01) # my range of X values, 
     #rangex=np.linspace(-5,5,10)
     plt.xlabel("X")
     plt.ylabel("Y")
     Dfxn = derivative(fxn,X,dx=1,n=1)
     Ifxn=odeint(h, 0, X)
     plt.plot(X,fxn(X),'r',label='Function',lw =2)
     plt.plot(X,Dfxn,'g',label='Derivative',lw =2)
     plt.plot(X,Ifxn,'bo',label='Integral',lw =2)
     
     plt.legend()
     plt.show()
	
