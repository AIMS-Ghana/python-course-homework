#!/usr/bin/python3

import matplotlib.pylab as plt
import numpy as np
from scipy.misc import derivative

def plotter(fxn):
     plt.figure()
     X = np.arange(0,10,0.01)
     plt.xlabel("X")
     plt.ylabel("Y")
     Dfxn = derivative(fxn,X,dx=1,n=1)
     plt.plot(X,fxn(X),'r',lw =2)
     plt.plot(X,Dfxn,'g',lw =2)
     plt.show()
