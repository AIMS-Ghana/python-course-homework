#!/usr/bin/python3

import matplotlib.pylab as plt
import numpy as np
from scipy.misc import derivative
from scipy.integrate import odeint

def calculus_plotter(fxn):
     def m(I,x):
        return fxn(x)



     plt.figure()
     X = np.arange(0,10.01,0.01)
     plt.xlabel("X")
     plt.ylabel("Y")
     Diff_fxn = derivative(fxn,X,dx=1,n=1)
     Inte_fxn = odeint(m, 0, X)
     plt.plot(X,fxn(X),'r',label="function",lw=2)
     plt.plot(X,Diff_fxn,'g',label="derivative",lw=2)
     plt.plot(X,Inte_fxn,'b',label="integral",lw=2)
     
     plt.legend()
     plt.show()




